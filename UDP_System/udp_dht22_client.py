import socket

SERVER_IP = "10.140.135.225"
SERVER_PORT = 2222
BUFFER_SIZE = 1024

print("Starting...")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_sock:
        print("Type 'temp' for temperature, 'hum' for humidity, 'exit' to quit.")

        while True:
            command = input("Enter command: ").strip().lower()
            client_sock.sendto(command.encode(), (SERVER_IP, SERVER_PORT))

            if command == "exit":
                print("Exiting client.")
                break

            data, server_addr = client_sock.recvfrom(BUFFER_SIZE)
            print(f"From server {server_addr[0]}:{server_addr[1]} -> {data.decode()}")

except KeyboardInterrupt:
    print("\nClient stopped manually. Exiting...")
