import socket
import sys
import random
import time

server_ip = '' 
server_port  = 7000

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(5):  
    data = ("Hello World!" * random.randrange(1, 10)).encode()
    udp_client_socket.sendto(data, (server_ip, server_port))

    try:
        data, addr = udp_client_socket.recvfrom(4096)
        if len(data) > 0:
            print(data.decode())

    except Exception:
        pass

    time.sleep(random.randrange(1, 10))

udp_client_socket.close()
