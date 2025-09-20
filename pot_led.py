import RPi.GPIO as GPIO 
import time 
from mcp3008 import MCP3008

GPIO.setmode(GPIO.BCM)

LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)

adc = MCP3008(vref=3.3)

try:
    while True: 
        raw_value = adc.read(0)
        duty_cycle = (raw_value / 1023) * 100 
        pwm.ChangeDutyCycle(duty_cycle)
        
        print(f"Pot ADC: {raw_value:4d}  Duty Cycle: {duty_cycle:.1f}%")

        time.sleep(0.5)
    
except KeyboardInterrupt: 
    print("Exiting...")

finally:
    pwm.stop()
    GPIO.cleanup()
    adc.close()
