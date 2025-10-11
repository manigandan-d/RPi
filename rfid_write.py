from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()

# print("Starting...")

try:
    text = input("Enter text to write to your RFID tag: ")
    print("Place your tag near the reader...")
    reader.write(text)
    print(f"Data '{text}' has been written successfully!")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
