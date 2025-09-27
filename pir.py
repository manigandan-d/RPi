import RPi.GPIO as GPIO
import time

PIR_PIN = 17 

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

time.sleep(5)

print("Starting...")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected")

        else:
            print("No motion")
        
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
