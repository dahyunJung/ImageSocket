import socket
import sys

# 소켓 생성하기
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓 연결하기
port = 80
host_ip = "127.0.0.1"

s.connect((host_ip, port))

s.send('난 client'.encode('utf-8'))

data = s.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))
