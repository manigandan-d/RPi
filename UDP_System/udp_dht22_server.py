import socket
import adafruit_dht
import board
import time

dht_device = adafruit_dht.DHT22(board.D4)

SERVER_IP = "10.140.135.225" 
SERVER_PORT = 2222
BUFFER_SIZE = 1024

def get_sensor_data():
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity
        return temperature_c, humidity
    
    except RuntimeError as e:
        print(f"Sensor error: {e}")
        return None, None

print("Starting...")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_sock:
        server_sock.bind((SERVER_IP, SERVER_PORT))
        print(f"Server listening on {SERVER_IP}:{SERVER_PORT}...")

        while True:
            message, client_addr = server_sock.recvfrom(BUFFER_SIZE)
            command = message.decode().strip().lower()
            print(f"Request from {client_addr[0]}:{client_addr[1]} -> {command}")

            if command == "exit":
                print("Client requested exit. Closing server.")
                break

            # Get fresh sensor data
            temp, hum = get_sensor_data()
            if temp is None or hum is None:
                reply = "Error: Could not read sensor"
            elif command == "temp":
                reply = f"Temperature: {temp:.1f} °C"
            elif command == "hum":
                reply = f"Humidity: {hum:.1f} %"
            else:
                reply = "Unknown command. Use 'temp' or 'hum'."

            server_sock.sendto(reply.encode(), client_addr)
            print(f"Sent -> {reply}")

except KeyboardInterrupt:
    print("\nServer stopped manually. Exiting...")

finally:
    dht_device.exit()
