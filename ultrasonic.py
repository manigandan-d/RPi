import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24 

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("Starting...")

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    duration = end_time - start_time

    distance = (34300 * duration) / 2

    return distance

try:
    while True: 
        dist = get_distance()
        print(f"Distance: {dist:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
