import socket
HOST = "127.0.0.1"
PORT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'b10932005')
    data = s.recv(1024)

print(data.decode())
