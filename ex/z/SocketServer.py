import socket

HOST = 'localhost'
PORT = 8081

serverSk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSk.bind((HOST, PORT))
serverSk.listen(1)

connectionSk, addr = serverSk.accept()
print(str(addr), ' 접속')

data = connectionSk.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

connectionSk.send('server.'.encode('utf-8'))
print('server 메시지를 보냈습니다.')