import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM) 

LED_PIN = 10    # GPIO18 
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)

print("Starting...")

try: 
    while True: 
        for duty in range(0, 101, 5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.05)

        for duty in range(100, -1, -5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.05)

except KeyboardInterrupt:
    print("Exiting...")

finally: 
    pwm.stop()
    GPIO.cleanup()
