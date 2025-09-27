from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)   # PCF8574 = I2C I/O expander, 0x27 = I2C address

lcd.cursor_pos = (0, 1)
lcd.write_string("Hello, World!")

lcd.crlf()

# lcd.clear()

lcd.cursor_pos = (1, 6) 
lcd.write_string("Pi")

lcd.cursor_mode = 'blink' 

# Custom character (smiley face)
smiley = (
    0b00000,
    0b01010,
    0b01010,
    0b00000,
    0b10001,
    0b01110,
    0b00000,
    0b00000,
)
lcd.create_char(0, smiley)
lcd.write_string("\x00")  # Print custom char
