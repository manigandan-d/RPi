import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)

SERVO_PIN = 18
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

print("Starting...")

def set_angle(angle):
    duty_cycle = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty_cycle)

try: 
    while True: 
        for angle in range(0, 181, 5):
            print(f"Moving to {angle}°")
            set_angle(angle)
            time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    pwm.stop()
    GPIO.cleanup()
