import socket

# Server configuration
SERVER_IP = "10.140.135.225"   # Raspberry Pi IP
SERVER_PORT = 2222
BUFFER_SIZE = 1024

# print("Starting...")

try:
    # Create UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_sock:
        server_sock.bind((SERVER_IP, SERVER_PORT))
        print(f"Server listening on {SERVER_IP}:{SERVER_PORT}...")

        # Wait for client message
        message, client_addr = server_sock.recvfrom(BUFFER_SIZE)
        print(f"Received from client {client_addr[0]}:{client_addr[1]} -> {message.decode()}")

        # Send reply
        reply = "Hello from server"
        server_sock.sendto(reply.encode(), client_addr)
        print("Reply sent to client.")

except KeyboardInterrupt:
    print("\nServer stopped manually. Exiting...")
