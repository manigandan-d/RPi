from picamera2 import Picamera2
import cv2
import time

# Coordinates for ROI
x1, y1 = 200, 100
x2, y2 = 400, 300

picam2 = Picamera2()

picam2.preview_configuration.main.size = (640, 480)  
picam2.preview_configuration.main.format = "RGB888"   
picam2.preview_configuration.align()                  
picam2.configure("preview")                           

picam2.start()
time.sleep(1) 

print("Press 'q' to quit")

while True:
    frame = picam2.capture_array()  

    roi = frame[y1:y2, x1:x2]

    # Rectangle for visualization
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("Original Image with ROI", frame)
    cv2.imshow("Extracted ROI", roi)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
