from pyzxing import BarCodeReader

# Initialize the ZXing reader
reader = BarCodeReader()

# Path to your MaxiCode image
image_path = r"C:\Users\user\OneDrive\Desktop\Y3-Notes\Robotics\__pdf417_decoder__\image.png"

# Decode the image
results = reader.decode(image_path)

# Print results 
if results:
    for result in results:
        print("Format:", result.get("format"))
        print("Data:", result.get("parsed"))
else:
    print("No MaxiCode found or could not be decoded.")
