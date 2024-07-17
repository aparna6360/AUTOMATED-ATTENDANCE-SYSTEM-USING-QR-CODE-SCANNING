# AUTOMATED-ATTENDANCE-SYSTEM-USING-QR-CODE-SCANNING

**Overview**
------------

The QR Code Student Attendance System is a Flask-based web application designed to streamline and automate attendance tracking for students using QR codes. The system utilizes computer vision and QR code scanning technology to mark attendance efficiently and accurately. This project is ideal for educational institutions looking to enhance their attendance management processes.

**Key Features**
--------------

1. QR Code Generation:

* Each student is assigned a unique QR code containing their name and student ID.
* The QR codes are generated using the qrcode library and saved as images in the static/images directory.

2. Real-time QR Code Scanning:

* The application uses OpenCV to capture video from a webcam.
* The pyzbar library is employed to decode QR codes in real-time from the video feed.
* Decoded QR data is processed to mark attendance, ensuring that each student is marked present only once.

3. Attendance Marking :

* When a QR code is scanned, the system logs the attendance by writing the student's name, ID, and timestamp to a CSV file (attendance.csv).
* The system also prints messages to the console to indicate whether attendance has been marked or if it has already been recorded for a particular student.

4.Web Interface:

* The Flask framework is used to create a web interface for the system.
* The home page (index.html) displays the live video feed for QR code scanning and the generated QR codes for each student.
* An absentees page (absentees.html) lists students who have not been marked present.
  

**Workflow**
-------------

1. Initialization:

* On application startup, QR codes for all students are generated and saved in the static/images directory.
* If an existing attendance.csv file is present, it is deleted to start fresh.
  
2. Home Page:

* The main interface displays the live video feed for real-time QR code scanning.
* The page also lists the generated QR codes for each student for easy reference.
  
3. Real-time Scanning:

* The system continuously captures video frames from the webcam.
* QR codes detected in the video frames are decoded, and the corresponding attendance is marked.
  
4. Attendance Marking:

* Upon decoding a QR code, the system extracts the student’s details and logs the attendance if not already marked.
* Attendance records are saved with timestamps in attendance.csv.
  
5. Absentees Page:

* The absentees page lists all students who have not been marked present during the session.
* This page helps in quickly identifying students who are absent.
  
6. Technologies Used

* Flask: For creating the web application and handling HTTP routes.
* OpenCV: For capturing and processing video frames from the webcam.
* pyzbar: For decoding QR codes from the video feed.
* qrcode: For generating unique QR codes for each student.
* HTML/CSS: For designing the web interface.
* CSV: For logging attendance data.


   
