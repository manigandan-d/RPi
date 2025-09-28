import RPi.GPIO as GPIO 
import time 
import adafruit_dht 
import board 
from RPLCD.i2c import CharLCD 
from mcp3008 import MCP3008

GPIO.setmode(GPIO.BCM)

BUTTON = 17
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

BUZZER = 18 
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.output(BUZZER, GPIO.LOW)  # Based on pnp/npn transistor, the value will change 

dhtDevice = adafruit_dht.DHT22(board.D4)

lcd = CharLCD("PCF8574", 0x27)

adc = MCP3008(vref=3.3)

mode = "program"
set_temp = 25.0 
prev_btn_state = GPIO.LOW

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
            adc_value = adc.read(0)
            set_temp = 15 + (adc_value / 1023) * 25 
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Program Mode")
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"Set Temp: {set_temp:4.1f}C")

        elif mode == "monitor":
            try:
                temp_c = dhtDevice.temperature 
                hum = dhtDevice.humidity 
                lcd.cursor_pos = (0, 0)
                lcd.write_string(f"T:{temp_c:4.1f}C H:{hum:4.1f}%")
                lcd.cursor_pos = (1, 0)
                lcd.write_string(f"Set: {set_temp:4.1f}C")

                if temp_c is not None and temp_c >= set_temp:
                    GPIO.output(BUZZER, GPIO.HIGH)

                else:
                    GPIO.output(BUZZER, GPIO.LOW)

            except RuntimeError as e:
                print("Retrying...", e)
                time.sleep(2)
                continue

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    adc.close()
    lcd.clear()
    GPIO.cleanup()
