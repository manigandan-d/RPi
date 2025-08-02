import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)

LED_PIN = 17
BTN_PIN = 18

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

led_state = False
prev_btn_state = GPIO.LOW

print("Starting...")

try:
    while True:
        cur_state = GPIO.input(BTN_PIN)

        if cur_state == GPIO.HIGH and prev_btn_state == GPIO.LOW: 
            time.sleep(0.2)

            if GPIO.input(BTN_PIN) == GPIO.HIGH: 
                led_state = not led_state
                GPIO.output(LED_PIN, led_state)

        prev_btn_state = cur_state
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Exiting...")

finally: 
    GPIO.cleanup()
