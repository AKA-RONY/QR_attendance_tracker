
from MyQRcode import myqr
import base64
import os

# Read the student names from the file
with open('student_data.txt', 'r') as f:
    names = f.readlines()

# Generate QR codes for each name
for name in names:
    # Encode the name in Base64 format for QR code generation
    name_encoded = base64.b64encode(name.encode('utf-8'))
    # Generate the QR code
    version, level, qr_name = myqr.run(
        words=name_encoded.decode('utf-8'),
        version=1,
        level='H',
        picture='a1.png',
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name=f'{name.strip()}.png',
        save_dir=os.getcwd()
    )
    print(f'Generated QR code for {name.strip()}')
