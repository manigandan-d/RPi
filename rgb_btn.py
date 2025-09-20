import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)

RED_PIN   = 17      # GPIO17 (pin 11)
GREEN_PIN = 27      # GPIO27 (pin 13)
BLUE_PIN  = 22      # GPIO22 (pin 15)

RED_BTN   = 5       # GPIO5 (pin 29) 
GREEN_BTN = 6       # GPIO6 (pin 31)
BLUE_BTN  = 13      # GPIO13 (pin 33)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

GPIO.setup(RED_BTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GREEN_BTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BLUE_BTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

red_state = False
green_state = False
blue_state = False

prev_red_btn = GPIO.LOW
prev_green_btn = GPIO.LOW
prev_blue_btn = GPIO.LOW

GPIO.output(RED_PIN, red_state)
GPIO.output(GREEN_PIN, green_state)
GPIO.output(BLUE_PIN, blue_state)

print("Starting...")

try:
    while True: 
        cur_red_btn = GPIO.input(RED_BTN)
        if cur_red_btn == GPIO.HIGH and prev_red_btn == GPIO.LOW:
            red_state = not red_state
            GPIO.output(RED_PIN, red_state)
        prev_red_btn = cur_red_btn

        cur_green_btn = GPIO.input(GREEN_BTN)
        if cur_green_btn == GPIO.HIGH and prev_green_btn == GPIO.LOW:
            green_state = not green_state
            GPIO.output(GREEN_PIN, green_state)
        prev_green_btn = cur_green_btn

        cur_blue_btn = GPIO.input(BLUE_BTN)
        if cur_blue_btn == GPIO.HIGH and prev_blue_btn == GPIO.LOW:
            blue_state = not blue_state
            GPIO.output(BLUE_PIN, blue_state)
        prev_blue_btn = cur_blue_btn

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
