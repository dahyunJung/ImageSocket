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
        print('server: ', recvData.decode('utf-8'))

clientSk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSk.connect((HOST, PORT))
print('연결 성공')

sender = threading.Thread(target=send, args=(clientSk, ))
receiver = threading.Thread(target=receive, args=(clientSk, ))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass

# https://foxtrotin.tistory.com/272