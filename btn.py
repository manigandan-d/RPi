import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

BTN_PIN = 18
GPIO.setup(BTN_PIN, GPIO.IN)
# GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try: 
    while True:
        if GPIO.input(BTN_PIN) == GPIO.HIGH:
            print("Button Pressed")

        else:
            print("Button Released")
        
        time.sleep(0.2)
    
except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
