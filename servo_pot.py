import RPi.GPIO as GPIO 
import time 
from mcp3008 import MCP3008

GPIO.setmode(GPIO.BCM)

SERVO_PIN = 18
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

adc = MCP3008(vref=3.3)

print("Starting...")

def set_angle(angle):
    duty_cycle = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty_cycle)

try:
    while True:
        adc_value = adc.read(0)

        angle = (adc_value / 1023) * 180
        set_angle(angle)

        print(f"ADC: {adc_value:4d}  ->  Angle: {angle:6.1f}°")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    pwm.stop()
    GPIO.cleanup()
    adc.close()
