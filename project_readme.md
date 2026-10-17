# Vision-Based Air Canvas

A CBSE Class 12 Computer Science project built using Python, OpenCV, MediaPipe, MySQL, and computer vision.

## Project Overview
This project creates a digital drawing application that allows users to draw in the air using hand gestures captured by a webcam. The system uses hand-tracking technology to detect finger movements and maps them to drawing actions such as drawing and erasing.

## Features
- User registration and login using MySQL
- Real-time webcam-based hand tracking
- Drawing using the index finger
- Erasing using index finger + middle finger
- Session log history saved to a local file
- Simple and interactive user interface
- Real-time digital canvas

## Technologies Used
- Python
- OpenCV
- MediaPipe
- MySQL Connector
- NumPy
- Pickle

## Project Structure
- main.py: main application logic
- setup.sql: database setup script
- requirements.txt: Python dependencies
- models/hand_landmarker.task: MediaPipe hand tracking model
- user_logs.dat: session logs saved during use

## Setup Instructions
1. Start your local MySQL server.
2. Import and run setup.sql in MySQL Workbench or another SQL client.
3. Install required dependencies:
   pip install -r requirements.txt
4. Run the application:
   python main.py

## Controls and shortcuts
- Draw (gesture): raise index finger alone for ~3 frames to start drawing
- Erase (gesture): raise index + middle for ~3 frames to erase
- Undo: `z`
- Redo: `y`
- Clear canvas: `x`
- Save canvas image: `s` (saved in `saved/` folder beside `main.py`)
- Brush size: `+` / `-`
- Color presets: press `1`..`5`
- Blackboard mode: press `b` to toggle a plain blackboard background; a yellow pointer circle shows fingertip location

## How It Works
- The webcam captures the live video stream.
- MediaPipe detects hand landmarks from the frame.
- The system checks the position of the fingertip.
- When the index finger is raised, the app draws.
- When the index and middle fingers are raised together, the app erases.
- The user can register or login before starting the drawing session.

## Security Note
This project is meant for educational demonstration. Passwords are stored as plain text to demonstrate database operations for a school project. It should not be used with real-world sensitive data.

## Applications
- Human-computer interaction
- Gesture-based digital drawing
- Classroom technology demonstration
- AI and computer vision learning

## Conclusion
The Vision-Based Air Canvas project demonstrates how computer vision can be used to create a natural and interactive user experience. It combines real-time gesture recognition, database handling, and practical programming in a single application.
