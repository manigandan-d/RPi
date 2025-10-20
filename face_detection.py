from picamera2 import Picamera2
import cv2
import time

picam2 = Picamera2()

picam2.preview_configuration.main.size = (1280, 720)  
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")

picam2.start()
time.sleep(1)

print("Press 'q' to quit")

face_cascade = cv2.CascadeClassifier("./haar/haarcascade_frontalface_default.xml")

while True:
    frame = picam2.capture_array()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
