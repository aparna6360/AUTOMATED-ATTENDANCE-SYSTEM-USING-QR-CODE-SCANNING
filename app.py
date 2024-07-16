from flask import Flask, render_template, Response, request, redirect, url_for
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import csv
import datetime
import qrcode
import os

app = Flask(__name__)

marked_attendance = set()
already_printed = set()
printed = set()

# List of students
students = [
    {"name": "Aparna K P", "student_id": "DS01"},
    {"name": "Amitha Chand", "student_id": "DS02"},
    {"name": "Indhu C N", "student_id": "DS03"},
    {"name": "Akash Krishna", "student_id": "DS04"},
    {"name": "Swaminathan T P", "student_id": "DS05"},
    {"name": "Visakh K Suresh", "student_id": "DS06"},
    {"name": "Christy Elizabeth", "student_id": "DS07"},
    {"name": "Anjana P", "student_id": "DS08"},
    {"name": "Abhishek M S", "student_id": "DS09"},
    {"name": "Aswin S", "student_id": "DS10"}
]

# Function to generate QR codes for each student
def generate_qr_codes():
    for student in students:
        unique_data = f"Name: {student['name']}, ID: {student['student_id']}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(unique_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(f"static/images/{student['student_id']}_qrcode.png")
        print(f"QR code generated for {student['name']}, ID: {student['student_id']}")

# Function to mark attendance
def mark_attendance(data):
    try:
        details = data.split(', ')
        name = details[0].split(': ')[1]
        student_id = details[1].split(': ')[1]
        if student_id in marked_attendance:
            if student_id not in already_printed:
                print(f"Attendance already marked for {name}, ID: {student_id}")
                already_printed.add(student_id)
            return

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open('attendance.csv', 'a', newline='') as csvfile:
            fieldnames = ['Name', 'Student ID', 'Timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Name': name, 'Student ID': student_id, 'Timestamp': timestamp})

        if student_id not in printed:
            print(f"Attendance marked for {name}, ID: {student_id}")
            printed.add(student_id)

        marked_attendance.add(student_id)
    except Exception as e:
        print(f"Error processing QR Code data: {e}")

# Delete the existing attendance.csv file on startup, if it exists
if os.path.exists('attendance.csv'):
    os.remove('attendance.csv')
    
# firstly Generate QR codes 
generate_qr_codes()

# Route to display the home page
@app.route('/')
def index():
    return render_template('index.html', students=students)

# Route to handle video stream
def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            mark_attendance(qr_data)
            points = np.array([obj.polygon], np.int32)
            points = points.reshape((-1, 1, 2))
            cv2.polylines(frame, [points], True, (0, 255, 0), 3)
            x, y, w, h = obj.rect
            cv2.putText(frame, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route to show absentees
@app.route('/absentees')
def show_absentees():
    absentees = [student for student in students if student['student_id'] not in marked_attendance]
    num_absentees = len(absentees)
    return render_template('absentees.html', absentees=absentees, num_absentees=num_absentees)

if __name__ == '__main__':
    app.run(debug=True)



