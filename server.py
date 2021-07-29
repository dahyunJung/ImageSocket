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

cam = cv2.VideoCapture("1215.mp4")
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
 
while True:
    # 제대로 읽으면 ret = True, 실패면 ret = False, frame에는 읽은 프레임
    ret, frame = cam.read()

    # encode_param의 형식으로 frame을 jpg로 이미지를 인코딩한다.
    result, frame = cv2.imencode('.jpg', frame, encode_param)

    # frame을 String 형태로 변환
    data = numpy.array(frame)

    #stringData = data.tostring() tobytes()를 권함
    stringData = data.tobytes()
 
    conn.sendall((str(len(stringData))).encode().ljust(16) + stringData)


#cv2.imwrite("image.jpg", frame)