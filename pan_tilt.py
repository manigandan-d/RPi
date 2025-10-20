from picamera2 import Picamera2
import cv2
import time
import numpy as np
from servo import Servo

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

pan = Servo(gpio_pin=13)
tilt = Servo(gpio_pin=12)

pan_angle = 0
tilt_angle = 0

pan.set_angle(pan_angle)
tilt.set_angle(tilt_angle)

print("Tracking enabled - Press 'q' to quit")

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
    detected = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.circle(frame, (disp_w//2, disp_h//2), 5, (255, 0, 255), -1)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        obj_cx = x + w // 2
        obj_cy = y + h // 2
        center_x = disp_w // 2
        center_y = disp_h // 2

        pan_error  = obj_cx - center_x
        tilt_error = obj_cy - center_y

        pan_angle -= pan_error // 75
        tilt_angle += tilt_error //75

        pan_angle  = max(min(pan_angle,  90), -90)
        tilt_angle = max(min(tilt_angle, 40), -90)

        if abs(pan_error) > 35:
            pan.set_angle(pan_angle)
        if abs(tilt_error) > 35:
            tilt.set_angle(tilt_angle)

    cv2.imshow("Camera", frame)
    cv2.imshow("Mask", cv2.resize(mask, (disp_w//2, disp_h//2)))
    cv2.imshow("Detected", cv2.resize(detected, (disp_w//2, disp_h//2)))

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('p'):
        print("Center HSV:", frame_hsv[disp_h//2, disp_w//2])

picam2.stop()
cv2.destroyAllWindows()
