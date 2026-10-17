"""Vision-Based Air Canvas Paint Application for a CBSE Class 12 project."""

import getpass
import os
import pickle
from datetime import datetime

import cv2
import mediapipe as mp
import mysql.connector
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# Keep the model and session file beside this program.
PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE = os.path.join(PROJECT_FOLDER, "models", "hand_landmarker.task")
LOG_FILE = os.path.join(PROJECT_FOLDER, "user_logs.dat")


def db_connect(password):
    """Connect to the local AirPaintDB MySQL database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=password,
            database="AirPaintDB"
        )
        print("Connected to the AirPaintDB database.")
        return connection
    except mysql.connector.Error as error:
        print("Could not connect to MySQL:", error)
        print("Check that MySQL is running and setup.sql has been run.")
        return None


def register_user(connection):
    """Add a new username and password to the users table."""
    if connection is None:
        print("Registration is unavailable because MySQL is not connected.")
        return

    username = input("Choose a username: ").strip()
    password = getpass.getpass("Choose a password: ")

    if username == "" or password == "":
        print("Username and password cannot be blank.")
        return

    cursor = connection.cursor()

    try:
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()
        print("Registration complete.")
    except mysql.connector.Error as error:
        print("Registration failed:", error)
    finally:
        cursor.close()


def login_user(connection):
    """Check the entered username and password against MySQL."""
    if connection is None:
        print("Login is unavailable because MySQL is not connected.")
        return None

    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")
    cursor = connection.cursor()

    try:
        query = """
            SELECT username
            FROM users
            WHERE username = %s AND password = %s
        """
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result is not None:
            print("Login successful.")
            return result[0]

        print("Incorrect username or password.")
        return None
    except mysql.connector.Error as error:
        print("Login failed:", error)
        return None
    finally:
        cursor.close()


def save_log(username, pixels_drawn, strokes_made):
    """Append one painting-session record to the binary pickle file."""
    record = {
        "Username": username,
        "Date/Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Pixels Drawn": pixels_drawn,
        "Strokes Made": strokes_made
    }

    try:
        with open(LOG_FILE, "ab") as file:
            pickle.dump(record, file)
        print("Painting session saved to user_logs.dat.")
    except OSError as error:
        print("Could not save the session log:", error)


def read_log():
    """Read and print all saved session records."""
    if not os.path.exists(LOG_FILE):
        print("There is no painting history yet.")
        return

    print("\nPast Painting Sessions")

    try:
        with open(LOG_FILE, "rb") as file:
            record_number = 1

            while True:
                try:
                    record = pickle.load(file)
                    print("Session", record_number)
                    print("  Username:", record["Username"])
                    print("  Date/Time:", record["Date/Time"])
                    print("  Pixels Drawn:", record["Pixels Drawn"])
                    print("  Strokes Made:", record["Strokes Made"])
                    record_number += 1
                except EOFError:
                    break

            if record_number == 1:
                print("There are no saved sessions.")
    except (OSError, pickle.UnpicklingError, KeyError) as error:
        print("Could not read the session history:", error)


def start_paint_canvas():
    """Open the webcam and use simple finger gestures to draw or erase."""
    if not os.path.exists(MODEL_FILE):
        print("Hand Landmarker model was not found:", MODEL_FILE)
        return None

    camera = None
    pixels_drawn = 0
    strokes_made = 0

    try:
        # Configure MediaPipe to process one hand in video mode.
        base_options = python.BaseOptions(model_asset_path=MODEL_FILE)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.VIDEO,
            num_hands=1
        )

        with vision.HandLandmarker.create_from_options(options) as landmarker:
            camera = cv2.VideoCapture(0)

            if not camera.isOpened():
                print("Could not open the webcam.")
                return None

            canvas = None
            previous_point = None
            window_name = "Air Canvas"
            last_timestamp_ms = 0

            # New state: undo/redo stacks and drawing controls
            undo_stack = []
            redo_stack = []
            max_undo = 10

            brush_color = (0, 255, 0)
            brush_size = 5
            color_presets = {
                "1": (0, 255, 0),  # green
                "2": (0, 0, 255),  # red
                "3": (255, 0, 0),  # blue
                "4": (0, 0, 0),    # black (useful for drawing on white saved backgrounds)
                "5": (255, 255, 255)  # white (for special use)
            }

            saved_dir = os.path.join(PROJECT_FOLDER, "saved")
            os.makedirs(saved_dir, exist_ok=True)

            # Blackboard mode: when True, show a plain black background and pointer
            blackboard_mode = False

            # Gesture stability and smoothing
            required_frames = 3
            # Require a longer hold for the open-palm "clear" gesture to avoid accidental clears
            required_frames_clear = 8
            draw_counter = 0
            erase_counter = 0
            clear_counter = 0
            stroke_active = False
            prev_smoothed = None
            smooth_alpha = 0.6

            def push_state():
                # Push a copy of the current canvas to the undo stack
                if canvas is None:
                    return
                if len(undo_stack) >= max_undo:
                    undo_stack.pop(0)
                undo_stack.append(canvas.copy())
                # Clearing redo when new action happens
                redo_stack.clear()

            def undo():
                nonlocal canvas
                if not undo_stack:
                    return
                redo_stack.append(canvas.copy())
                canvas = undo_stack.pop()

            def redo():
                nonlocal canvas
                if not redo_stack:
                    return
                undo_stack.append(canvas.copy())
                canvas = redo_stack.pop()

            def clear_canvas():
                nonlocal canvas
                if canvas is None:
                    return
                push_state()
                canvas[:] = 0

            def save_canvas():
                filename = datetime.now().strftime("aircanvas_%Y%m%d_%H%M%S.png")
                path = os.path.join(saved_dir, filename)
                try:
                    cv2.imwrite(path, canvas)
                    print("Saved canvas to", path)
                    return path
                except Exception as e:
                    print("Could not save image:", e)
                    return None

            while True:
                success, frame = camera.read()

                if not success:
                    print("Could not read a frame from the webcam.")
                    break

                # Mirror the camera image so hand movement feels natural.
                frame = cv2.flip(frame, 1)
                height, width = frame.shape[:2]

                if canvas is None:
                    canvas = np.zeros((height, width, 3), dtype=np.uint8)

                # MediaPipe Tasks accepts an RGB image.
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                mp_image = mp.Image(
                    image_format=mp.ImageFormat.SRGB,
                    data=rgb_frame
                )

                timestamp_ms = int(
                    cv2.getTickCount() * 1000 / cv2.getTickFrequency()
                )
                timestamp_ms = max(timestamp_ms, last_timestamp_ms + 1)
                last_timestamp_ms = timestamp_ms
                result = landmarker.detect_for_video(mp_image, timestamp_ms)

                if result.hand_landmarks:
                    hand = result.hand_landmarks[0]

                    # Compare each fingertip with the joint below it.
                    index_up = hand[8].y < hand[6].y
                    middle_up = hand[12].y < hand[10].y
                    ring_up = hand[16].y < hand[14].y
                    pinky_up = hand[20].y < hand[18].y

                    raw_x = int(hand[8].x * width)
                    raw_y = int(hand[8].y * height)
                    raw_x = max(0, min(raw_x, width - 1))
                    raw_y = max(0, min(raw_y, height - 1))

                    # Smooth fingertip position to reduce jitter
                    if prev_smoothed is None:
                        sm_x, sm_y = raw_x, raw_y
                    else:
                        sm_x = int(prev_smoothed[0] * (1 - smooth_alpha) + raw_x * smooth_alpha)
                        sm_y = int(prev_smoothed[1] * (1 - smooth_alpha) + raw_y * smooth_alpha)
                    prev_smoothed = (sm_x, sm_y)
                    point = (sm_x, sm_y)

                    # Debounce gestures: require N consecutive frames
                    is_draw_gesture = index_up and not middle_up and not ring_up and not pinky_up
                    is_erase_gesture = index_up and middle_up and not ring_up and not pinky_up
                    is_clear_gesture = index_up and middle_up and ring_up and pinky_up

                    if is_draw_gesture:
                        draw_counter += 1
                    else:
                        draw_counter = 0

                    if is_erase_gesture:
                        erase_counter += 1
                    else:
                        erase_counter = 0

                    if is_clear_gesture:
                        clear_counter += 1
                    else:
                        clear_counter = 0

                    active_mode = None
                    if draw_counter >= required_frames:
                        active_mode = "draw"
                    elif erase_counter >= required_frames:
                        active_mode = "erase"
                    elif clear_counter >= required_frames_clear:
                        active_mode = "clear"

                    # Handle mode transitions and strokes
                    if active_mode == "draw":
                        if not stroke_active:
                            push_state()
                            strokes_made += 1
                            stroke_active = True
                            previous_point = point
                        else:
                            # Count approximate pixels
                            pixels_drawn += max(abs(point[0] - (previous_point or point)[0]),
                                                abs(point[1] - (previous_point or point)[1]))
                            start_point = previous_point or point
                            cv2.line(canvas, start_point, point, brush_color, brush_size)
                            previous_point = point

                    elif active_mode == "erase":
                        if stroke_active:
                            stroke_active = False
                        # Erase by drawing a filled circle in black (canvas background)
                        cv2.circle(canvas, point, max(10, brush_size * 3), (0, 0, 0), -1)
                        previous_point = None

                    elif active_mode == "clear":
                        # Clear canvas on open palm (debounced)
                        push_state()
                        clear_canvas()
                        # reset counters to avoid repeated clears
                        clear_counter = 0
                        draw_counter = 0
                        erase_counter = 0
                        previous_point = None

                    else:
                        # No active mode
                        if stroke_active:
                            stroke_active = False
                        previous_point = None
                else:
                    previous_point = None

                # Blend the drawing with the mirrored camera image or show blackboard
                if blackboard_mode:
                    # Show only the canvas on a black background
                    display_frame = canvas.copy()
                else:
                    display_frame = cv2.addWeighted(frame, 1.0, canvas, 0.7, 0)

                # Compact overlay: two-line summary of state and controls
                mode_text = 'Draw' if draw_counter >= required_frames else ('Erase' if erase_counter >= required_frames else ('Clear' if clear_counter >= required_frames_clear else 'Idle'))
                cv2.putText(display_frame, f"Mode:{mode_text}  Brush:{brush_size}  Color:{brush_color}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)
                cv2.putText(display_frame, "z=Undo  y=Redo  x=Clear  s=Save  +/- size  1-5 color  b=Blackboard", (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (200, 200, 200), 1)

                # Draw pointer circle at fingertip to indicate location
                if prev_smoothed is not None:
                    cv2.circle(display_frame, prev_smoothed, max(5, brush_size // 2), (0, 255, 255), 2)
                cv2.imshow(window_name, display_frame)

                key = cv2.waitKey(1) & 0xFF

                # Keyboard shortcuts
                if key == ord('q'):
                    break
                elif key == ord('z'):
                    undo()
                elif key == ord('y'):
                    redo()
                elif key == ord('x'):
                    clear_canvas()
                elif key == ord('+') or key == ord('='):
                    brush_size = min(100, brush_size + 1)
                elif key == ord('-'):
                    brush_size = max(1, brush_size - 1)
                elif key == ord('s'):
                    save_canvas()
                elif chr(key) in color_presets:
                    brush_color = color_presets.get(chr(key), brush_color)
                elif key == ord('b'):
                    # Toggle blackboard mode
                    blackboard_mode = not blackboard_mode
                    if blackboard_mode:
                        # Ensure canvas is black when enabling
                        if canvas is not None:
                            canvas[:] = 0
                    else:
                        # Clear overlay text a bit by pushing state
                        push_state()

                # Also stop when the user closes the camera window.
                if cv2.getWindowProperty(
                    window_name, cv2.WND_PROP_VISIBLE
                ) < 1:
                    break

        return pixels_drawn, strokes_made

    except Exception as error:
        print("The painting session could not run:", error)
        return None
    finally:
        if camera is not None:
            camera.release()
        cv2.destroyAllWindows()


def authentication_menu(connection):
    """Show the console menu before starting the webcam."""
    while True:
        print("\nAir Canvas Menu")
        print("1. Register a new user")
        print("2. Login")
        print("3. View Past Painting Session History")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_user(connection)
        elif choice == "2":
            username = login_user(connection)
            if username is not None:
                return username
        elif choice == "3":
            read_log()
        elif choice == "4":
            return None
        else:
            print("Please enter 1, 2, 3, or 4.")


def main():
    # Database access is attempted before any webcam window is opened.
    database_password = getpass.getpass(
        "Enter the MySQL root password (press Enter if none): "
    )
    connection = db_connect(database_password)

    try:
        username = authentication_menu(connection)

        if username is None:
            print("Goodbye.")
            return

        session_data = start_paint_canvas()

        if session_data is not None:
            pixels_drawn, strokes_made = session_data
            save_log(username, pixels_drawn, strokes_made)
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    main()