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

red_pwm = GPIO.PWM(RED_PIN, 1000)
green_pwm = GPIO.PWM(GREEN_PIN, 1000)
blue_pwm = GPIO.PWM(BLUE_PIN, 1000)

red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

red_dc = 0.99
green_dc = 0.99
blue_dc = 0.99

prev_red_btn = GPIO.LOW
prev_green_btn = GPIO.LOW
prev_blue_btn = GPIO.LOW

print("Starting...")

try:
    while True: 
        cur_red_btn = GPIO.input(RED_BTN)
        if cur_red_btn == GPIO.HIGH and prev_red_btn == GPIO.LOW:
            red_dc = red_dc * 1.58
            if red_dc > 99: 
                red_dc = 0.99
            red_pwm.ChangeDutyCycle(int(red_dc))
            print(f"Red brightness: {int(red_dc)}%")
        prev_red_btn = cur_red_btn

        cur_green_btn = GPIO.input(BLUE_BTN)
        if cur_green_btn == GPIO.HIGH and prev_green_btn == GPIO.LOW:
            green_dc = green_dc * 1.58
            if green_dc > 99:
                green_dc = 0.99
            green_pwm.ChangeDutyCycle(int(green_dc))
            print(f"Green brightness: {int(green_dc)}%")
        prev_green_btn = cur_green_btn

        cur_blue_btn = GPIO.input(BLUE_BTN)
        if cur_blue_btn == GPIO.HIGH and prev_blue_btn == GPIO.LOW:
            blue_dc = blue_dc * 1.58
            if blue_dc > 99: 
                blue_dc = 0.99
            blue_pwm.ChangeDutyCycle(int(blue_dc))
            print(f"Blue brightness: {int(blue_dc)}%")
        prev_blue_btn = cur_blue_btn

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()
