import RPi.GPIO as GPIO
import time

IR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)

print("Starting...")

try:
    while True:
        if GPIO.input(IR_PIN) == 0:
            print("Object Detected!")
        else:
            print("No Object")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
