import cv2

# ✅ Option 1: use a raw string
image = cv2.imread(r"C:\Users\user\OneDrive\Desktop\Y3-Notes\Robotics\__pdf417_decoder__\Screenshot 2025-11-02 184714.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detector = cv2.QRCodeDetector()
data, bbox, rectified_image = detector.detectAndDecode(gray)

if data:
    print("Decoded data:", data)
else:
    print("No QR code detected")

if bbox is not None:
    for i in range(len(bbox)):
        cv2.line(image, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), (0, 255, 0), 2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
