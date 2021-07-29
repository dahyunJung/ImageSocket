# server

import socket
import cv2
import numpy as np
 
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
 
HOST=''
PORT=9594

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)
print('Socket now listening')
 
#연결, conn에는 소켓 객체, addr은 소켓에 바인드 된 주소
conn,addr=s.accept()
 
while True:
    length = recvall(conn, 16)
    stringData = recvall(conn, int(length))
    data = np.frombuffer(stringData, dtype = 'uint8')
    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)

    cv2.imshow('ImageWindow',frame)
    cv2.waitKey(1)


#cv2.imwrite("image.jpg", frame)