# Vision-Based Air Canvas

A CBSE Class 12 Computer Science practical project using Python, OpenCV,
MediaPipe Hand Landmarker, MySQL, and pickle binary-file handling.

## Project files

- `main.py` runs the terminal menu, login, webcam canvas, and session history.
- `setup.sql` creates the `AirPaintDB` database and `users` table.
- `requirements.txt` lists the Python packages used by the program.
- `models/hand_landmarker.task` is the MediaPipe hand tracking model.

## Setup

1. Start the local MySQL server.
2. Run `setup.sql` in MySQL Workbench or a MySQL client.
3. Install the Python packages from this folder:

   ```text
   pip install -r requirements.txt
   ```

4. Start the program:

   ```text
   python main.py
   ```

The program asks for the MySQL `root` password in the terminal. Choose
registration or login from the menu. In the camera window, raise only the
index finger to draw and raise the index and middle fingers to erase. Press
`q` or `c`, or close the camera window, to finish the session.

Painting history is appended to `user_logs.dat` beside `main.py`. The
session's drawn-pixel count is an estimate based on the movement between
successive fingertip positions.

## Classroom security note

This simple demonstration stores passwords as plain text to show basic SQL
registration and login. Do not use it to store real account passwords.