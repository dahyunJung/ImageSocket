import cv2
import socket
import numpy
 
HOST = '127.0.0.1'
PORT = 8585

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
print('Socket now listening')

while True:
    #연결, conn에는 소켓 객체, addr은 소켓에 바인드 된 주소
    conn, addr=s.accept()
    print(addr)

    #cam = cv2.VideoCapture('1215.mp4')
    #encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]

    #ret, frame = cam.read()
    #result, frame = cv2.imencode('.jpg', frame, encode_param)

    # frame을 String 형태로 변환
    #data = numpy.array(frame)
    #stringData = data.toString()
    stringData = 'hello'.encode('utf-8')
        
    # s.sendall((str(len(stringData))).encode().ljust(16) + stringData)
    s.send(stringData)
    #cam.release()

conn.close()


'''
import cv2
import socket
import numpy
 
HOST = '127.0.0.1'
PORT = 8585


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


## webcam 이미지 capture
cam = cv2.VideoCapture('1215.mp4')
 
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
 
while True:
    ret, frame = cam.read()
    # frame을 jpg로 이미지를 인코딩한다.
    result, frame = cv2.imencode('.jpg', frame, encode_param)

    # frame을 String 형태로 변환
    data = numpy.array(frame)
    stringData = data.toString()
    
    # s.sendall((str(len(stringData))).encode().ljust(16) + stringData)
    s.send(stringData)
 
cam.release()
'''



'''
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
PORT=8585

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)
print('Socket now listening')
 
#연결, conn에는 소켓 객체, addr은 소켓에 바인드 된 주소
conn,addr=s.accept()
 
while True:
    # client에서 받은 stringData의 크기 (==(str(len(stringData))).encode().ljust(16))
    length = recvall(conn, 16)
    stringData = recvall(conn, int(length))
    data = np.fromstring(stringData, dtype = 'uint8')
    
    #data를 디코딩한다.
    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
    cv2.imshow('ImageWindow',frame)
    cv2.waitKey(1)
'''