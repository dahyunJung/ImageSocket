import socket
import threading
import time

HOST = 'localhost'
PORT = 8081

def send(sk):
    while True:
        sendData = input('>>>')
        sk.send(sendData.encode('utf-8'))

def receive(sk):
    while True:
        recvData = sk.recv(1024)
        print('client: ', recvData.decode('utf-8'))


serverSk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSk.bind((HOST, PORT))
serverSk.listen(1)

print('%d번 포트 접속 대기..' % PORT)

connectionSk, addr = serverSk.accept()
print(str(addr), ' 접속')

sender = threading.Thread(target=send, args=(connectionSk, ))
receiver = threading.Thread(target=receive, args=(connectionSk, ))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass

# https://foxtrotin.tistory.com/272