import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import time

# Create and read the attendance file
attendance_file = open('attendance_sheet.txt', 'a+')
attendance_list = attendance_file.read().split('\n')

# Start the webcam
cap = cv2.VideoCapture(0)

# Function to enter data in attendance filerun
def enter_data(data):
    if data in attendance_list:
        print('Already Marked Present')
    else:
        attendance_list.append(data)
        attendance_file.write(data+'\n')
        print('Marked Present')

# Function to check data in QR code
def check_data(decoded_objects):
    for obj in decoded_objects:
        data = obj.data.decode('ascii')
        enter_data(data)

# Main loop to read QR code from webcam and mark attendance
while True:
    # Capture the frame from webcam
    _, frame = cap.read()

    # Decode the QR code from the frame
    decoded_objects = pyzbar.decode(frame)

    # Check if the data is already present in attendance file or not
    check_data(decoded_objects)

    # Display the frame
    cv2.imshow('QR Code Scanner', frame)

    # Exit the program if user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()
attendance_file.close()
