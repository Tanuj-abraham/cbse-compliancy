# Vision-Based Air Canvas

## Project Synopsis

### Title
Vision-Based Air Canvas using Python and OpenCV

### Abstract
The project aims to develop a vision-based drawing application where a user can draw in the air using hand gestures captured through a webcam. The system uses computer vision and machine learning to detect hand movements and interpret them as drawing actions. It allows users to perform basic actions such as drawing and erasing using finger gestures, making the application interactive and innovative.

The project is implemented using Python, OpenCV, MediaPipe, and MySQL. It also includes user registration and login, which enhances the system by enabling personalized session tracking. The project demonstrates the use of real-time image processing, gesture recognition, database connectivity, and file-based logging in a practical application.

### Objectives
- To design an application that allows drawing using hand gestures
- To integrate real-time computer vision for finger tracking
- To provide a simple and interactive interface using webcam input
- To store user information in a MySQL database
- To maintain painting session history for each user
- To create a practical project based on AI and computer vision

### Problem Statement
Traditional drawing tools require direct physical contact with a mouse or pen. This project solves that limitation by allowing users to write or draw in the air using hand gestures captured by a camera. This creates a more natural and futuristic interface, especially useful in presentations and educational demonstrations.

### Methodology
1. The webcam captures live video frames.
2. The image is processed with OpenCV.
3. MediaPipe detects hand landmarks and identifies finger positions.
4. The system checks whether the index finger is raised for drawing and whether the index and middle fingers are raised for erasing.
5. The positions of finger tips are tracked to draw strokes on the canvas.
6. User information is stored in the MySQL database.
7. Session details are saved in a log file for future reference.

### Technologies Used
- Python
- OpenCV
- MediaPipe
- MySQL
- NumPy
- Pickle

### Applications
- Digital art creation
- Interactive classroom demonstrations
- Gesture-based human-computer interaction
- Educational and presentation tools
- AI and vision-based automation projects

### Future Scope
- Add brush color and size controls
- Add undo/redo features
- Save output as image file
- Add voice or gesture-based commands
- Improve gesture recognition accuracy
