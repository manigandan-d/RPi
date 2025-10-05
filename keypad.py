import RPi.GPIO as GPIO 
import time 

class Keypad:
    def __init__(self, row_pins, col_pins, keys):
        self.row_pins = row_pins
        self.col_pins = col_pins
        self.keys = keys

        GPIO.setmode(GPIO.BCM)

        for row in self.row_pins:
            GPIO.setup(row, GPIO.OUT)
            GPIO.output(row, GPIO.LOW)

        for col in self.col_pins:
            GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def get_key(self):
        for r in range(len(self.row_pins)):
            GPIO.output(self.row_pins[r], GPIO.HIGH)
            for c in range(len(self.col_pins)):
                if GPIO.input(self.col_pins[c]) == GPIO.HIGH:
                    time.sleep(0.3)
                    GPIO.output(self.row_pins[r], GPIO.LOW)
                    return self.keys[r][c]
            GPIO.output(self.row_pins[r], GPIO.LOW)
        return None
    
    def cleanup(self):
        GPIO.cleanup()
