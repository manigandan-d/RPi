from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()

# print("Starting...")

try:
    print("Place your RFID tag near the reader...")
    id, text = reader.read()
    print(f"UID: {id}")
    print(f"Stored Text: {text.strip()}")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
