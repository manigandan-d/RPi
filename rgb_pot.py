import RPi.GPIO as GPIO 
import time 
from mcp3008 import MCP3008

GPIO.setmode(GPIO.BCM)

RED_PIN = 17 
GREEN_PIN = 27 
BLUE_PIN = 22 

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

red_pwm = GPIO.PWM(RED_PIN, 1000)
green_pwm = GPIO.PWM(GREEN_PIN, 1000)
blue_pwm = GPIO.PWM(BLUE_PIN, 1000)

red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

adc = MCP3008(vref=3.3)

print("Starting...")

try: 
    while True:
        red_value = adc.read(0)
        green_value = adc.read(1)
        blue_value = adc.read(2)

        red_dc = (red_value / 1023) * 100
        green_dc = (green_value / 1023) * 100
        blue_dc = (blue_value / 1023) * 100 

        red_pwm.ChangeDutyCycle(red_dc)
        green_pwm.ChangeDutyCycle(green_dc)
        blue_pwm.ChangeDutyCycle(blue_dc)

        print(f"R: {red_dc:.1f}%  G: {green_dc:.1f}%  B: {blue_dc:.1f}%")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()
    adc.close()
