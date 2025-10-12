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

while True:
    frame = picam2.capture_array()  
    cv2.imshow("Raspberry Pi Camera Feed", frame)  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
