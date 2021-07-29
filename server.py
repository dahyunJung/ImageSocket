# server

import socket
import cv2
import numpy
 
HOST='127.0.0.1'        # jetson ip
PORT=9594

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)
print('listen')
 
#연결, conn에는 소켓 객체, addr은 소켓에 바인드 된 주소
conn,addr=s.accept()

try:
    cam = cv2.VideoCapture("1215.mp4")
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    
    while True:
        ret, frame = cam.read()    # frame에는 읽은 프레임
        result, frame = cv2.imencode('.jpg', frame, encode_param)    # frame을 jpg로 이미지 인코딩.
        data = numpy.array(frame)    # frame을 String 형태로 변환
        #print(data)        #[[255] \n [216] ...]
        stringData = data.tobytes()    # tostring() tobytes()를 권함
        # print(stringData)     # /x12
    
        conn.sendall((str(len(stringData))).encode().ljust(16) + stringData)
        #conn.sendall(stringData)
except:
    print('cancel')

#cv2.imwrite("image.jpg", frame)