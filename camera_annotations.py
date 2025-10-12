from picamera2 import Picamera2
import cv2
import time

picam2 = Picamera2()

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

# Text settings
FONT_FACE = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.8
FONT_COLOR = (0, 255, 0)  # Green text
FONT_THICKNESS = 2
POS_FPS = (10, 40)
POS_RES = (10, 75)

# Annotation parameters
RECT_COLOR = (255, 0, 0)    # Blue rectangle
CIRCLE_COLOR = (0, 0, 255)  # Red circle
THICKNESS = 2

picam2.preview_configuration.main.size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate = 60
picam2.preview_configuration.align()
picam2.configure("preview")

picam2.start()
time.sleep(1)

print("Press 'q' to quit")

fps = 0.0
alpha = 0.1  # smoothing factor for FPS

while True:
    start_time = time.time()

    frame = picam2.capture_array()

    # Draw a rectangle
    cv2.rectangle(frame, (100, 100), (400, 300), RECT_COLOR, THICKNESS)

    # Draw a circle
    cv2.circle(frame, (700, 250), 80, CIRCLE_COLOR, THICKNESS)

    # Draw a filled rectangle
    cv2.rectangle(frame, (50, 400), (250, 600), (0, 125, 255), -1)

    # Draw a line
    cv2.line(frame, (600, 100), (1200, 300), (255, 255, 0), 3)

    # Draw an ellipse
    cv2.ellipse(frame, (500, 500), (100, 50), 30, 0, 360, (0, 255, 255), 2)

    cv2.putText(frame, f"FPS: {int(fps)}", POS_FPS, FONT_FACE, FONT_SCALE, FONT_COLOR, FONT_THICKNESS)
    cv2.putText(frame, f"Res: {DISPLAY_WIDTH}x{DISPLAY_HEIGHT}", POS_RES, FONT_FACE, FONT_SCALE, FONT_COLOR, FONT_THICKNESS)

    cv2.imshow("Raspberry Pi Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    elapsed_time = time.time() - start_time
    if elapsed_time > 0:
        current_fps = 1.0 / elapsed_time
        fps = (1 - alpha) * fps + alpha * current_fps

picam2.stop()
cv2.destroyAllWindows()
