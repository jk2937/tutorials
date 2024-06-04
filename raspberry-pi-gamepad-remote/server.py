import socket

ip = ''
port = 7000

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.setblocking(False)  # Non-blocking mode
udp_server_socket.bind((ip, port))

print(f"Echo server started on {ip}:{port}")

while True:
    try:
        data, addr = udp_server_socket.recvfrom(4096)
        if len(data) > 0:
            print(data.decode())
            udp_server_socket.sendto(data, addr)

    except Exception:
        pass 
