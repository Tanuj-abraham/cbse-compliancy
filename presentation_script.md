# Presentation Script for Vision-Based Air Canvas

## Introduction
Good morning everyone. Today I am presenting my Computer Science project titled “Vision-Based Air Canvas”. This project is based on computer vision and allows a user to draw in the air using hand gestures captured by a webcam.

## What is the project?
The project uses a webcam to detect hand movement and interprets finger gestures to draw on a digital canvas. It allows users to perform actions like drawing and erasing without using a mouse or touch screen.

## Why is this project useful?
This project is useful because it demonstrates how artificial intelligence and image processing can be used in real-life applications. It is interactive, interesting, and can be used in presentations, digital art, and classroom demonstrations.

## Technologies used
The project is built using Python, OpenCV, MediaPipe, MySQL, and NumPy. Python is used for programming logic, OpenCV is used for image processing, and MediaPipe detects hand landmarks. MySQL is used to store user information such as username and password.

## How does it work?
The webcam captures a live video stream. The application processes each frame and identifies the hand landmarks. When the index finger is raised, the system treats it as drawing mode. The system tracks the fingertip movement and draws a line on the screen. When the index and middle fingers are raised together, the system enters erase mode and removes the content around the fingertip.

## Demo steps and controls
1. Run `python main.py` and login or register.
2. The camera window shows the live feed and the drawing canvas overlay.
3. Demonstrate drawing: raise the index finger alone for a moment (drawing starts after 3 consecutive frames).
4. Demonstrate erasing: raise index + middle fingers together (erase starts after 3 consecutive frames).
5. Use keyboard shortcuts during the demo: `z` undo, `y` redo, `x` clear, `s` save image, `+`/`-` change brush size, `1`–`5` change color preset.
6. Optional: press `b` to switch to a blackboard view; a yellow pointer will show fingertip location for precise pointing during the demo.

## Database part
The project also includes a login and registration system using MySQL. A user can create an account and then log in before starting the drawing session. This adds security and real-world relevance to the project.

## Session history
The system also stores the session details such as username, date, number of pixels drawn, and total strokes. This is useful for tracking user activity and demonstrates file handling and data storage.

## Advantages
This project is simple, interactive, and innovative. It combines multiple areas of Computer Science such as image processing, database management, and programming logic. It is also a good example of practical application of modern technologies.

## Limitations
The system depends on webcam quality and light conditions. In poor lighting or cluttered backgrounds, gesture detection may become less accurate. Still, the project works well in normal conditions.

## Conclusion
In conclusion, the Vision-Based Air Canvas project shows how gesture recognition can be used to create a digital drawing system. It is a practical and creative solution that combines technology, user interaction, and problem solving. Thank you.
