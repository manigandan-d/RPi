import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24 

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("Starting...")

def measure_time():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    return end_time - start_time

try:
    while True: 
        d_cm = float(input("Enter distance to object (in cm): "))
        d_m = d_cm / 100.0 

        round_trip = 2 * d_m 

        duration = measure_time() 
        speed = round_trip / duration

        print(f"Measured Speed of Sound: {speed:.2f} m/s")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
