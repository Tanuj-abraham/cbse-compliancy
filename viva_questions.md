# Viva Questions and Answers

## Q1. What is the project about?
This project is a vision-based drawing system where users can draw in the air using hand gestures captured by a webcam. It converts finger motion into drawing actions on a digital canvas.

## Q2. Why did you choose this project?
This project combines areas like computer vision, artificial intelligence, and database management. It is innovative, practical, and relevant to the current trend of smart human-computer interaction.

## Q3. What technology is used for hand tracking?
The project uses MediaPipe Hand Landmarker, which detects hand landmarks from live video frames.

## Q4. How does drawing work?
The system tracks the position of the index fingertip. When the index finger is raised and the other fingers are not, the program draws a line from the previous point to the current point.

## Q5. How does erasing work?
When the index and middle fingers are raised together, the system interprets it as erase mode and removes pixels in a circular region around the fingertip.

## Q6. How is the user login implemented?
The project uses MySQL to store usernames and passwords. The program connects to a local MySQL database and checks the entered credentials against the data stored in the users table.

## Q7. Why is MySQL used?
MySQL is used to store user data securely in a structured database, making the project more real-world and practical than simple file-based storage.

## Q8. What is the role of OpenCV?
OpenCV is used to capture video from the webcam, process frames, display the canvas, and overlay text and drawing on the video feed.

## Q9. What is the significance of the project?
It shows how computer vision can be used to create intuitive user interfaces without physical devices such as a mouse or touchscreen.

## Q10. What are the limitations of the project?
The project relies on a webcam, good lighting, and proper hand positioning. It may also not detect gestures accurately in poor lighting or when multiple objects are in the frame.

## Q11. How can the project be improved?
It can be improved by adding color selection, undo/redo options, brush size control, image export, and better gesture recognition. (These enhancements have been implemented: keyboard+gesture controls, undo/redo (`z`/`y`), clear (`x`), save (`s`), brush size `+`/`-`, color presets `1`–`5`, and gesture debounce/smoothing.)

## Q12. What is the main contribution of your project?
The main contribution is creating a gesture-based digital drawing system that makes user interaction more natural and futuristic.
