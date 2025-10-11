import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TOUCH_PIN = 17
GPIO.setup(TOUCH_PIN, GPIO.IN)

print("Starting...")

try:
    while True:
        if GPIO.input(TOUCH_PIN):
            print("Touched!")

        else:
            print("Not touched.")
        
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
