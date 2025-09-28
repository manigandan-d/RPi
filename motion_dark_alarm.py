import RPi.GPIO as GPIO 
import time 
from RPLCD.i2c import CharLCD 
from mcp3008 import MCP3008

DEFAULT_DARK_THRESHOLD = 300 

GPIO.setmode(GPIO.BCM)

BUTTON = 17
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

BUZZER = 18 
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.output(BUZZER, GPIO.LOW)  # Based on pnp/npn transistor, the value will change 

PIR = 24
GPIO.setup(PIR, GPIO.IN)

lcd = CharLCD("PCF8574", 0x27)
lcd.clear()

adc = MCP3008(vref=3.3)

mode = "program"
dark_threshold = DEFAULT_DARK_THRESHOLD
prev_btn_state = GPIO.LOW

time.sleep(2)

print("Starting...")

try:
    while True:
        cur_btn_state = GPIO.input(BUTTON)
        if cur_btn_state == GPIO.HIGH and prev_btn_state == GPIO.LOW:
            mode = "monitor" if mode == "program" else "program"
            GPIO.output(BUZZER, GPIO.LOW)
            lcd.clear()
            time.sleep(0.2)
        prev_btn_state = cur_btn_state

        if mode == "program":
            dark_threshold = round(adc.read(0))
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Program Mode")
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"Dark Thrld: {dark_threshold}")

        elif mode == "monitor":
            pir = GPIO.input(PIR)
            ldr_value = round(adc.read(1))
            lcd.cursor_pos = (0, 0)
            lcd.write_string(f"LDR Val: {ldr_value}")
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"Dark Thrld: {dark_threshold}")

            is_dark = ldr_value < dark_threshold

            if pir and is_dark:
                GPIO.output(BUZZER, GPIO.HIGH)

            else:
                GPIO.output(BUZZER, GPIO.LOW)

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.output(BUZZER, GPIO.LOW)
    adc.close()
    lcd.clear()
    GPIO.cleanup()
