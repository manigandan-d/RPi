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

print("Press 's' to save image, 'q' to quit")

image_count = 1

while True:
    frame = picam2.capture_array()  
    cv2.imshow("Raspberry Pi Camera Feed", frame)  

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        filename = f"capture_{image_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
        image_count += 1

    elif key == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
