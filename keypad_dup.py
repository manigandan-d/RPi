import RPi.GPIO as GPIO 
import time 

ROW = 4
COL = 4

KEYPAD = [
    ['1', '2', '3', 'A'], 
    ['4', '5', '6', 'B'], 
    ['7', '8', '9', 'C'], 
    ['*', '0', '#', 'D']
]

GPIO.setmode(GPIO.BCM)

ROW_PINS = [5, 6, 13, 19]
COL_PINS = [12, 16, 20, 21]

for row in ROW_PINS:
    GPIO.setup(row, GPIO.output)
    GPIO.output(row, GPIO.LOW)

for col in COL_PINS:
    GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Starting...")

def read_keypad():
    for r in range(ROW):
        GPIO.output(ROW_PINS[r], GPIO.HIGH)
        for c in range(COL):
            if GPIO.input(COL_PINS[c]) == GPIO.HIGH:
                time.sleep(0.3)
                GPIO.output(ROW_PINS[r], GPIO.LOW)
                return KEYPAD[r][c]
        GPIO.output(ROW_PINS[r], GPIO.LOW)

try:
    print("Press keys on the keypad:")

    while True:
        key = read_keypad()    
        if key:
            print(f"Key Pressed: {key}")
        time.sleep(0.2)


except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
