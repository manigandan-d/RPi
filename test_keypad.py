from keypad import Keypad 
import time 

KEYPAD = [
    ['1', '2', '3', 'A'], 
    ['4', '5', '6', 'B'], 
    ['7', '8', '9', 'C'], 
    ['*', '0', '#', 'D']
]

ROW_PINS = [5, 6, 13, 19]
COL_PINS = [12, 16, 20, 21]

print("Starting...")

keypad = Keypad(ROW_PINS, COL_PINS, KEYPAD)

try:
    print("Press keys on the keypad:")

    while True:
        key = keypad.get_key()    
        if key:
            print(f"Key Pressed: {key}")
        time.sleep(0.1)


except KeyboardInterrupt:
    print("Exiting...")

finally:
    keypad.cleanup()
