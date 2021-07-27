# sever가 client로 부터 이미지를 얻는다.
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
 
HOST=''     # 자신의 컴 ip
PORT=8485

#TCP 사용
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
print('Socket now listening')

#연결, conn에는 소켓 객체, addr은 소켓에 바인드 된 주소
conn, addr=s.accept()

while True:
# client에서 받은 stringData의 크기 (==(str(len(stringData))).encode().ljust(16))
    #xc = conn.recv(len(s))
    #a = np.fromstring()

    length = recvall(conn, 6)       # buf 크기
    stringData = recvall(conn, int(length))     # byte 데이터
    data = np.fromstring(stringData, dtype = 'uint8')    
    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)    #data를 디코딩한다.

    cv2.imshow('ImageWindow',frame)
    cv2.waitKey(1)