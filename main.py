from pdf417decoder import PDF417Decoder
from PIL import Image

# Load the image
image_path = "23e8a677-dc0a-4c17-8c90-82540acfb4ff.png"

# Decode PDF417 barcode
decoder = PDF417Decoder(image_path)
decoder.decode()

# Get all decoded data
for barcode in decoder.barcode_data_list:
    print("Decoded Data:")
    print(barcode.data)
