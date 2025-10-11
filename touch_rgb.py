import RPi.GPIO as GPIO
import time

TOUCH_PIN = 17
RED_PIN = 27
GREEN_PIN = 22
BLUE_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TOUCH_PIN, GPIO.IN)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

GPIO.output(RED_PIN, GPIO.LOW)
GPIO.output(GREEN_PIN, GPIO.LOW)
GPIO.output(BLUE_PIN, GPIO.LOW)

state = 0
last_touch_time = 0
debounce_time = 0.3 

print("Starting...")

try:
    while True:
        if GPIO.input(TOUCH_PIN) == GPIO.HIGH:
            if time.time() - last_touch_time > debounce_time:
                state = (state + 1) % 4
                last_touch_time = time.time()
                print(f"Touch detected, state: {state}")

                GPIO.output(RED_PIN, GPIO.LOW)
                GPIO.output(GREEN_PIN, GPIO.LOW)
                GPIO.output(BLUE_PIN, GPIO.LOW)

                if state == 0:
                    print("LED OFF")
                elif state == 1:
                    GPIO.output(RED_PIN, GPIO.HIGH)
                    print("Red ON")
                elif state == 2:
                    GPIO.output(GREEN_PIN, GPIO.HIGH)
                    print("Green ON")
                elif state == 3:
                    GPIO.output(BLUE_PIN, GPIO.HIGH)
                    print("Blue ON")

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
