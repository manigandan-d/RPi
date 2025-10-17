from picamera2 import Picamera2
import cv2
import time
import numpy as np 

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
    inverted = 255 - frame 

    combined = np.hstack((frame, inverted))

    cv2.imshow("Original (left) + Inverted (right)", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
