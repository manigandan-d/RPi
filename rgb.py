import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)

RED_PIN   = 17      # GPIO17 (pin 11)
GREEN_PIN = 27      # GPIO27 (pin 13)
BLUE_PIN  = 22      # GPIO22 (pin 15)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

print("Starting...")

try:
    while True: 
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(BLUE_PIN, GPIO.LOW)
        time.sleep(1)

        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        GPIO.output(BLUE_PIN, GPIO.LOW)
        time.sleep(1)

        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(BLUE_PIN, GPIO.HIGH)
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
