import socket
HOST = "127.0.0.1"
PORT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        s.sendto(f"NTUST welcome {data.decode()}".encode(), addr)
