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

print("Press 'q' to quit | 'p' to print center HSV")

hue_low, hue_high = 30, 40
sat_low, sat_high = 100, 255
val_low, val_high = 100, 255

lower_bound = np.array([hue_low, sat_low, val_low])
upper_bound = np.array([hue_high, sat_high, val_high])

while True:
    frame = picam2.capture_array()

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
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
