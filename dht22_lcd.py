import RPi.GPIO as GPIO
import time
import adafruit_dht 
import board
from RPLCD.i2c import CharLCD

GPIO.setmode(GPIO.BCM)

SWITCH_PIN = 17
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_btn_state = GPIO.LOW

dhtDevice = adafruit_dht.DHT22(board.D4)

lcd = CharLCD('PCF8574', 0x27)
lcd.clear()

tempMode = False

print("Starting...")

try:
    while True:
        cur_btn_state = GPIO.input(SWITCH_PIN)
        if cur_btn_state == GPIO.HIGH and prev_btn_state == GPIO.LOW:
            tempMode = not tempMode
        prev_btn_state = cur_btn_state

        temp_c = dhtDevice.temperature
        humidity = dhtDevice.humidity

        if temp_c is not None and humidity is not None:
            if tempMode:
                temp_f = (temp_c * 9/5) + 32
                lcd.clear()
                lcd.write_string(f"Temp: {temp_f:.1f}F")
                lcd.crlf()
                lcd.write_string(f"Hum : {humidity:.1f}%")
                
            else:
                lcd.clear()
                lcd.write_string(f"Temp: {temp_c:.1f}C")
                lcd.crlf()
                lcd.write_string(f"Hum : {humidity:.1f}%")

        else:
            lcd.clear()
            lcd.write_string("Sensor Error")

        time.sleep(2) 

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
