import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIR_PIN = 17   
ALARM_PIN = 27 

GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(ALARM_PIN, GPIO.OUT)

time.sleep(5) 

try:
    while True:
        if GPIO.input(PIR_PIN): 
            print("Motion detected. Alarm ON")
            GPIO.output(ALARM_PIN, GPIO.HIGH)

        else:
            print("No motion. Alarm OFF")
            GPIO.output(ALARM_PIN, GPIO.LOW)

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
