from picamera2 import Picamera2
import cv2
import time
import numpy as np

# Display resolution
disp_w = 1280
disp_h = 720

picam2 = Picamera2()
picam2.preview_configuration.main.size = (disp_w, disp_h)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure(picam2.preview_configuration)

picam2.start()
time.sleep(1)

def nothing(x):
    pass

cv2.namedWindow("HSV Trackbars")

cv2.createTrackbar("Hue Low", "HSV Trackbars", 0, 179, nothing)
cv2.createTrackbar("Hue High", "HSV Trackbars", 179, 179, nothing)
cv2.createTrackbar("Sat Low", "HSV Trackbars", 0, 255, nothing)
cv2.createTrackbar("Sat High", "HSV Trackbars", 255, 255, nothing)
cv2.createTrackbar("Val Low", "HSV Trackbars", 0, 255, nothing)
cv2.createTrackbar("Val High", "HSV Trackbars", 255, 255, nothing)

print("Adjust HSV sliders. Press 'q' to quit.")

while True:
    frame = picam2.capture_array()
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    h_low = cv2.getTrackbarPos("Hue Low", "HSV Trackbars")
    h_high = cv2.getTrackbarPos("Hue High", "HSV Trackbars")
    s_low = cv2.getTrackbarPos("Sat Low", "HSV Trackbars")
    s_high = cv2.getTrackbarPos("Sat High", "HSV Trackbars")
    v_low = cv2.getTrackbarPos("Val Low", "HSV Trackbars")
    v_high = cv2.getTrackbarPos("Val High", "HSV Trackbars")

    lower_bound = np.array([h_low, s_low, v_low])
    upper_bound = np.array([h_high, s_high, v_high])

    mask = cv2.inRange(frame_hsv, lower_bound, upper_bound)
    object = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.circle(frame, (disp_w//2, disp_h//2), 5, (255, 0, 255), -1)

    cv2.imshow("Raspberry Pi Camera Feed", frame)
    cv2.imshow("Mask", cv2.resize(mask, (disp_w//2, disp_h//2)))
    cv2.imshow("Object", cv2.resize(object, (disp_w//2, disp_h//2)))

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('p'):
        print("Center HSV:", frame_hsv[disp_h//2, disp_w//2])

picam2.stop()
cv2.destroyAllWindows()
