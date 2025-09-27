import time
import adafruit_dht
import board

# DHT22 is connected to GPIO4 (pin 7)
dhtDevice = adafruit_dht.DHT22(board.D4)

try:
    while True:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity

        if temperature_c is not None and humidity is not None:
            temperature_f = temperature_c * 9 / 5 + 32
            print(f"Temp: {temperature_c:.1f}°C / {temperature_f:.1f}°F    Humidity: {humidity:.1f}%")
            
        else:
            print("Sensor reading failed. Try again.")

        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting...")
