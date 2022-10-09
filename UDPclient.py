import socket
HOST = "127.0.0.1"
PORT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'b10932005', (HOST, PORT))
    data, _ = s.recvfrom(1024)
    s.sendto(b'', (HOST, PORT))

print(data.decode())
