import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

BUZZER_PIN = 18 
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 440)
pwm.start(50) 

print("Starting...")

try:
    while True:
        for freq in range(400, 1001, 10):
            pwm.ChangeFrequency(freq)
            time.sleep(0.01)

        for freq in range(1000, 399, -10):
            pwm.ChangeFrequency(freq)
            time.sleep(0.01)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    pwm.stop()
    GPIO.cleanup()
