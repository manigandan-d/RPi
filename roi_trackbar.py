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

cv2.namedWindow("Trackbars")

cv2.createTrackbar("X Pos", "Trackbars", 10, disp_w-1, nothing)
cv2.createTrackbar("Y Pos", "Trackbars", 10, disp_h-1, nothing)
cv2.createTrackbar("Box Width", "Trackbars", 10, disp_w-1, nothing)
cv2.createTrackbar("Box Height", "Trackbars", 10, disp_h-1, nothing)

print("Press 'q' to quit")

while True:
    frame = picam2.capture_array()

    x_pos = cv2.getTrackbarPos("X Pos", "Trackbars")
    y_pos = cv2.getTrackbarPos("Y Pos", "Trackbars")
    box_w = cv2.getTrackbarPos("Box Width", "Trackbars")
    box_h = cv2.getTrackbarPos("Box Height", "Trackbars")

    roi = frame[y_pos:y_pos+box_h, x_pos:x_pos+box_w]

    cv2.rectangle(frame, (x_pos, y_pos), (x_pos+box_w, y_pos+box_h), (0, 0, 255), 2)

    cv2.imshow("Camera", frame)
    cv2.imshow("ROI", roi)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
