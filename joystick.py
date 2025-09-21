import RPi.GPIO as GPIO 
import time 
from mcp3008 import MCP3008

GPIO.setmode(GPIO.BCM)

SW_PIN = 23
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

adc = MCP3008(vref=3.3)

print("Starting...")

try: 
    while True:
        x_val = adc.read(0)
        y_val = adc.read(1)
        btn_state = GPIO.input(SW_PIN)

        print(f"X Value: {x_val}  Y Value: {y_val}  Button State: {btn_state}")

except KeyboardInterrupt: 
    print("Exiting...")

finally:
    GPIO.cleanup()
    adc.close()
