# Vision-Based Air Canvas

## Acknowledgement
I would like to express my sincere gratitude to my Computer Science teacher for guiding me throughout this project. I also thank my parents and friends for their support and encouragement. This project helped me understand the practical application of Python programming, computer vision, and database management.

## Introduction
The project titled “Vision-Based Air Canvas” is a gesture-based drawing system developed using Python. It uses a webcam to capture live hand movement and draws on the screen based on finger gestures. This project combines concepts of computer vision, database management, and user interaction in a simple and effective way.

## Aim
The aim of this project is to create a system where a user can draw on a digital canvas without using a physical mouse or pen, using only hand gestures captured by a webcam.

## Objectives
- To build a drawing system using real-time camera input
- To detect hand gestures using MediaPipe
- To implement drawing and erasing actions based on fingers
- To integrate MySQL for login and registration
- To maintain painting session records for users
- To create an interactive application using Python

## Hardware and Software Requirements
### Hardware
- Personal computer
- Webcam
- Internet connection for installing packages

### Software
- Python 3
- OpenCV
- MediaPipe
- MySQL Server
- NumPy
- MySQL Connector

## Tools and Technologies Used
- Python
- OpenCV
- MediaPipe
- MySQL
- NumPy
- pickle module

## Working Principle
The system captures live video frames using OpenCV. MediaPipe identifies the landmarks of the hand and tracks the finger positions. If the index finger is raised, the program interprets it as drawing mode, and a line is drawn from the previous finger position to the current one. If the index and middle fingers are raised together, the system interprets it as erase mode. The program records the user’s information in a MySQL database and stores painting details in a log file.

## Program Flow
1. The application starts with a menu.
2. The user chooses to register or login.
3. The system connects to the MySQL database.
4. Once logged in, the webcam starts.
5. The user draws using finger movement.
6. The session is saved in a log file after completion.

## Advantages
- No physical drawing device needed
- Interactive and innovative user interface
- Useful for presentations and demonstrations
- Combines multiple concepts of computer science
- Can be extended with more features in the future

## Limitations
- Works best in good lighting conditions
- Accuracy depends on webcam quality
- Slight delay may occur during tracking
- Gesture detection may be affected by background clutter

## Applications
- Human-computer interaction
- Classroom demonstrations
- Digital artwork creation
- AI and computer vision learning

## Conclusion
The Vision-Based Air Canvas project successfully demonstrates the use of computer vision and hand gestures for drawing. It is a practical and innovative application that combines Python programming, image processing, database connectivity, and user interaction. This project not only improves technical knowledge but also shows how AI and machine learning can be used in day-to-day applications.

## Bibliography
- OpenCV Documentation
- MediaPipe Documentation
- Python Official Documentation
- MySQL Documentation
- Computer Science practical project references
