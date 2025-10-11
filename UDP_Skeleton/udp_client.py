import socket

# Server (Raspberry Pi) configuration
SERVER_IP = "10.140.135.225"
SERVER_PORT = 2222
BUFFER_SIZE = 1024

print("Starting...")

try:
    # Create UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_sock:
        # Send message to server
        message = "Hello from client"
        client_sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
        print(f"Sent to server {SERVER_IP}:{SERVER_PORT} -> {message}")

        # Receive reply
        data, server_addr = client_sock.recvfrom(BUFFER_SIZE)
        print(f"Received from server {server_addr[0]}:{server_addr[1]} -> {data.decode()}")

except KeyboardInterrupt:
    print("\nClient stopped manually. Exiting...")
