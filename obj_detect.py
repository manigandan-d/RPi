from picamera2 import Picamera2
import cv2
import time
from tflite_support.task import core 
from tflite_support.task import processor  
from tflite_support.task import vision
import utils 

model = "efficientdet_lite0.tflite"
num_threads = 4

disp_w = 1280 
disp_h = 720 

picam2 = Picamera2()

picam2.preview_configuration.main.size = (disp_w, disp_h)  
picam2.preview_configuration.main.format = "RGB888"   
picam2.preview_configuration.align()                  
picam2.configure("preview")                           

picam2.start()
time.sleep(1) 

base_options = core.BaseOptions(file_name=model, use_coral=False, num_threads=num_threads)
detection_options = processor.DetectionOptions(max_results=8, score_threshold=0.3)
options = vision.ObjectDetectorOptions(base_options=base_options, detection_options=detection_options)
detector = vision.ObjectDetector.create_from_options(options)

print("Press 'q' to quit")

while True:
    frame = picam2.capture_array()  

    # rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_tensor = vision.TensorImage.create_from_array(frame)
    detections = detector.detect(frame_tensor)
    image = utils.visualize(frame, detections)

    cv2.imshow("Camera", frame)  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
