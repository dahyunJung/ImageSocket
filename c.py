#server 

import cv2
import socket

HOST = '127.0.0.1'
PORT = 8585

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(10)
print('Socket now listening')
 
#연결, conn에는 소켓 객체, addr은 소켓에 바인드 된 주소
conn,addr=s.accept()
 
while True:
    ## webcam 이미지 capture
    cam = cv2.VideoCapture('1215.mp4') 
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
    ret, frame = cam.read()

    # frame을 jpg로 이미지를 인코딩한다.
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    stringData = frame.tobytes()

    #print(stringData) # /x42
    
    s.sendall((str(len(stringData))).encode().ljust(16) + stringData)

cam.release()
