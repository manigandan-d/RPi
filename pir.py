import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIR_PIN = 17 
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
