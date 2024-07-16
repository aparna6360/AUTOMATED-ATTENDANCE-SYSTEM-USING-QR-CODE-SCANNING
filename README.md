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

   
