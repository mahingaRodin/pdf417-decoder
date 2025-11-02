from pyzbar.pyzbar import decode
from PIL import Image

image_path = "Screenshot 2025-11-02 182858.png"
decoded_objects = decode(Image.open(image_path))

for obj in decoded_objects:
    print("Type:", obj.type)
    print("Data:", obj.data.decode('utf-8', errors='ignore'))
