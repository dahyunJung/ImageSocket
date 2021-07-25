import socket

HOST = 'localhost'
PORT = 8081

clientSk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSk.connect((HOST, PORT))
print('연결 성공')

clientSk.send('client'.encode('utf-8'))
print('메시지 전송')

data = clientSk.recv(1024)
print('받은 데이터: ', data.decode('utf-8'))

# https://foxtrotin.tistory.com/272