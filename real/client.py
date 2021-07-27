import cv2
import socket
import numpy as np
 
HOST='127.0.0.1'     # 자신의 컴 ip
PORT=8485


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))       

cam = cv2.VideoCapture('1215.mp4')
 
while True:
    # frame에는 읽은 프레임
    ret, frame = cam.read()
    # frame을 jpg로 이미지를 인코딩한다.
    result, frame = cv2.imencode('.jpg', frame)
    # frame을 String 형태로 변환
    data = np.array(frame)
    stringData = data.tobytes()

    #print(len(stringData))
    #print(type(stringData))  bytes
    #print(stringData)
    
 
    #서버에 데이터 전송 (str(len(stringData))).encode().ljust(16)
    s.sendall((str(len(stringData))).encode().ljust(16) + stringData)

 
cam.release()
