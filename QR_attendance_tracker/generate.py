import qrcode
import cv2

# Read the student names from the file
with open('assets/student_data.txt', 'r') as f:
    names = f.readlines()

print(names)

# Generate QR codes for each name
for name in names:
    qr = qrcode.make(name)
    print(f'Generated QR code for {name.strip()}')
    qr.save('assets/QRs/img.png')


# Decoding the QR
# Name of the QR Code Image file
filename = "assets/QRs/img.png"

# read the QRCODE image
image = cv2.imread(filename)

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# detect and decode
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

# if there is a QR code
# print the data
if vertices_array is not None:
    print("QRCode data:")
    print(data)
