from picamera2 import Picamera2
import cv2
import time

picam2 = Picamera2()

display_width = 1280
display_height = 720

picam2.preview_configuration.main.size = (display_width, display_height)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate = 60
picam2.preview_configuration.align()
picam2.configure("preview")

picam2.start()
time.sleep(1)

print("Press 'q' to quit")

fps = 0

pos = (10, 40)
font_face = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 255, 0)
font_thickness = 2

x, y = 200, 200
radius = 40
dx, dy = 8, 6
color = (0, 0, 255)  # red

while True:
    start_time = time.time()

    frame = picam2.capture_array()

    x += dx
    y += dy

    if x - radius <= 0 or x + radius >= display_width:
        dx = -dx
    if y - radius <= 0 or y + radius >= display_height:
        dy = -dy

    cv2.circle(frame, (x, y), radius, color, -1)

    cv2.putText(frame, f"FPS: {int(fps)}", pos, font_face, font_scale, font_color, font_thickness)

    cv2.imshow("Raspberry Pi Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    end_time = time.time()
    elapsed_time = end_time - start_time
    fps = (0.9 * fps) + (0.1 * (1 / elapsed_time))

picam2.stop()
cv2.destroyAllWindows()
