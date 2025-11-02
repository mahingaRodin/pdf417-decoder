from pylibdmtx.pylibdmtx import decode
from PIL import Image

# Load the image
image_path = "Screenshot 2025-11-02 183821.png"

# Decode the Data Matrix code
decoded_objects = decode(Image.open(image_path))

# Print decoded data
if decoded_objects:
    for obj in decoded_objects:
        print("Decoded Data:")
        print(obj.data.decode('utf-8', errors='ignore'))
else:
    print("No Data Matrix code found in the image.")
