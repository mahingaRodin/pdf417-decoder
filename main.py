from pdf417decoder import PDF417Decoder
from PIL import Image

# Load the image
image_path = "Screenshot 2025-11-02 182858.png"

# Decode PDF417 barcode
decoder = PDF417Decoder(image_path)
decoder.decode()

# Get all decoded data
for barcode in decoder.barcode_data_list:
    print("Decoded Data:")
    print(barcode.data)
