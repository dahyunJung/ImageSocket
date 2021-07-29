# client

import cv2
import socket
import numpy
 
HOST = '127.0.0.1'
PORT = 9594

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))       

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
 
    #서버에 데이터 전송 (str(len(stringData))).encode().ljust(16)
    s.sendall((str(len(stringData))).encode().ljust(16) + stringData)
 
cam.release()
