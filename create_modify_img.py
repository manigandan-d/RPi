from picamera2 import Picamera2
import cv2
import time
import numpy as np 

picam2 = Picamera2()

picam2.preview_configuration.main.size = (1280, 720)  
picam2.preview_configuration.main.format = "RGB888"   
picam2.preview_configuration.align()                  
picam2.configure("preview")                           

picam2.start()
time.sleep(1) 

print("Press 'q' to quit")

# W = 640
# H = 480
img = np.zeros((480, 640, 3), dtype=np.uint8)
cv2.imshow("Blank Image", img)

img[:480//2, :640//2] = [0, 0, 255]
img[:480//2, 640//2:] = [0, 255, 0]
img[480//2:, :640//2] = [255, 0, 0]
img[480//2:, 640//2:] = [255, 255, 255]
cv2.imshow("Modified Image", img)

while True:
    frame = picam2.capture_array()  

    frame[100:200, 150:350] = [0, 255, 255]

    cv2.imshow("Raspberry Pi Camera Feed", frame)  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
