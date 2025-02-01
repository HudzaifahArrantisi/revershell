import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.0.100", 5500))
server_socket.listen(1)

print("Menunggu koneksi...")
client_socket, client_address = server_socket.accept()
print(f"Terhubung dengan {client_address}")

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Received: {data.decode('utf-8')}")

client_socket.close()
server_socket.close()