# QR_attendance_tracker


1. student_data.txt file has the name of students whose QR is to be generated [harsh,salvik,rohan] in this case
2. The generate.py file will generate the qr code for respective student and save the qr in .png format
3. frame_test.py is a sample file for testing whether the cv2 module is working properly and accessing the camera in a frame
4. The attend.py file will take the attendance using cv2 module for accessing webcam and pyzbar for decoding. 
5. The attendance_sheet.txt will hold all the attendance of the student after detecting the QR from user-end



###
the app should work as the way mentioned but , am facing an error where after running the attend.py file it cant detect the qr code, and throwing error.
(save the file in your directory and in that directory ,open cmd and run python attend.py , a frame will  open accessing your webcam .
send the Qr code to your mobile and scan it to the webcam. no respone will be given to attendance_sheet.txt. if left idle you will recive error decoding message.
try to debug the error see if it works

###

### Commands to start the dev server

```python
# Run the command in the root directory 

python -m QR_attendance_tracker

```
