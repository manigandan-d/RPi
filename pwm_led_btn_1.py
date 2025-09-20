import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)

LED_PIN   = 18    # GPIO18 (pin 12)
BTN_UP    = 23    # GPIO23 (pin 16)
BTN_DOWN  = 24    # GPIO24 (pin 18)

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BTN_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)

duty_cycle = 0

prev_up_state = GPIO.LOW
prev_down_state = GPIO.LOW

print("Starting...")

try: 
    while True: 
        cur_up_state = GPIO.input(BTN_UP)
        cur_down_state = GPIO.input(BTN_DOWN)

        if cur_up_state == GPIO.HIGH and prev_up_state == GPIO.LOW:
            if duty_cycle < 100:
                duty_cycle += 10
                pwm.ChangeDutyCycle(duty_cycle)
                print(f"Brightness Increased: {duty_cycle}%")

        if cur_down_state == GPIO.HIGH and prev_down_state == GPIO.LOW:
            if duty_cycle > 0: 
                duty_cycle -= 10 
                pwm.ChangeDutyCycle(duty_cycle)
                print(f"Brightness Decreased: {duty_cycle}%")

        prev_up_state = cur_up_state
        prev_down_state = cur_down_state

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    pwm.stop()
    GPIO.cleanup()
