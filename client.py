# client

import cv2
import socket
import numpy
 
#socket에서 수신한 버퍼를 반환하는 함수
def recvall(sock, count):
    # 바이트 문자열
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

HOST = '127.0.0.1'
PORT = 9594

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))       
print('connect')
 
while True:
    length = recvall(s, 16)
    stringData = recvall(s, int(length))
    data = numpy.frombuffer(stringData, dtype = 'uint8')
    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)

    cv2.imshow('ImageWindow',frame)
    cv2.waitKey(1)
 
cam.release()
