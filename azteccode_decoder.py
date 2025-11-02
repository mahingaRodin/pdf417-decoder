import cv2

# Load the image
image_path = r"C:\Users\user\OneDrive\Desktop\Y3-Notes\Robotics\__pdf417_decoder__\aztec_code.png"
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create the detector (works for QR and Aztec)
detector = cv2.wechat_qrcode_WeChatQRCode()  # Best accuracy
# Alternative if you don't want WeChat model downloads:
# detector = cv2.QRCodeDetector()

# Detect and decode
try:
    res, points = detector.detectAndDecode(gray)
    if isinstance(res, list) and res:
        print("Decoded Data:")
        for r in res:
            print(r)
    elif isinstance(res, str) and res:
        print("Decoded Data:", res)
    else:
        print("No Aztec code detected.")
except Exception as e:
    print("Error:", e)

# Optional: visualize detected area
if 'points' in locals() and points is not None and len(points) > 0:
    for p in points:
        pts = p.astype(int).reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 2)
    cv2.imshow("Detected Aztec Code", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
