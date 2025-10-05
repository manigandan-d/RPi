from keypad import Keypad 
import time 
from RPLCD.i2c import CharLCD

KEYPAD = [
    ['1', '2', '3', 'A'], 
    ['4', '5', '6', 'B'], 
    ['7', '8', '9', 'C'], 
    ['*', '0', '#', 'D']
]

ROW_PINS = [5, 6, 13, 19]
COL_PINS = [12, 16, 20, 21]

keypad = Keypad(ROW_PINS, COL_PINS, KEYPAD)

lcd = CharLCD('PCF8574', 0x27)
lcd.clear()

print("Starting...")

try:
    lcd.write_string("Press keys")

    while True:
        key = keypad.get_key()    
        if key:
            lcd.clear()
            lcd.write_string(f"Key Pressed: {key}")
        time.sleep(0.1)


except KeyboardInterrupt:
    print("Exiting...")

finally:
    lcd.clear()
    keypad.cleanup()
