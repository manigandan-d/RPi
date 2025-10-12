from picamera2 import Picamera2
import cv2
import time

picam2 = Picamera2()

# Display parameters
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

# Text overlay settings
POS = (10, 40)
FONT_FACE = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 1
FONT_COLOR = (0, 255, 0)  # Green
FONT_THICKNESS = 2

# Configure the preview mode
picam2.preview_configuration.main.size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate = 60  # Request 60 FPS
picam2.preview_configuration.align()
picam2.configure("preview")

picam2.start()
time.sleep(1) 

print("Press 'q' to quit")

fps = 0.0 
alpha = 0.1  # Smoothing factor for low-pass filter

while True:
    start_time = time.time()

    frame = picam2.capture_array()

    cv2.putText(frame, f"FPS: {int(fps)}", POS, FONT_FACE, FONT_SCALE, FONT_COLOR, FONT_THICKNESS)

    cv2.imshow("Raspberry Pi Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    elapsed_time = time.time() - start_time
    if elapsed_time > 0:
        current_fps = 1.0 / elapsed_time
        fps = (1 - alpha) * fps + alpha * current_fps  # Low-pass filtered FPS

picam2.stop()
cv2.destroyAllWindows()
