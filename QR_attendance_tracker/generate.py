import qrcode
import cv2

with open('C:/OAT[ ver-2]/QR_attendance_tracker/QR_attendance_tracker/static/assets/student_data.txt', 'r') as f:
    names = f.readlines()


def generateQR(names):
    names = [item.strip() for item in names]
    print(names)

    # Generate QR codes for each name
    for name in names:
        qr = qrcode.make(name)
        print(f'Generated QR code for {name}')
        qr.save(
            f"C:/OAT[ ver-2]/QR_attendance_tracker/QR_attendance_tracker/static/assets/QR/{name.split()[0]}.png")


def decodeQR(names):
    # Decoding the QR
    for name in names:

        # Name of the QR Code Image file
        filename = f"C:/OAT[ ver-2]/QR_attendance_tracker/QR_attendance_tracker/static/assets/QR/{name.split()[0]}.png"

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


if __name__ == '__main__':
    # Read the student names from the file/database
    with open('C:/OAT[ ver-2]/QR_attendance_tracker/QR_attendance_tracker/static/assets/student_data.txt', 'r') as f:
        names = f.readlines()

    generateQR(names)
    decodeQR(names)
