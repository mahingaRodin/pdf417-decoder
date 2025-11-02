from pyzbar.pyzbar import decode
from PIL import Image

# Load the image
image_path = "Screenshot 2025-11-02 184258.png"

# Decode barcode(s)
decoded_objects = decode(Image.open(image_path))

# Print all detected barcodes
if decoded_objects:
    for obj in decoded_objects:
        print("Barcode Type:", obj.type)
        print("Barcode Data:", obj.data.decode('utf-8', errors='ignore'))
else:
    print("No barcode detected in the image.")
