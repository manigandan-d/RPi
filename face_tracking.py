from picamera2 import Picamera2
import cv2
import time
from servo import Servo

picam2 = Picamera2()

disp_w = 1280 
disp_h = 720 

picam2.preview_configuration.main.size = (disp_w, disp_h)  
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")

picam2.start()
time.sleep(1)

pan = Servo(gpio_pin=13)
tilt = Servo(gpio_pin=12)

pan_angle = 0
tilt_angle = 0

pan.set_angle(pan_angle)
tilt.set_angle(tilt_angle)

print("Face Tracking Active - Press 'q' to quit")

face_cascade = cv2.CascadeClassifier("./haar/haarcascade_frontalface_default.xml")

while True:
    frame = picam2.capture_array()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

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

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
