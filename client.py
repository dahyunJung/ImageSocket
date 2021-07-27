# client가 server로 이미지를 보낸다.
import cv2
import socket
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8485))       

cam = cv2.VideoCapture('1215.mp4')

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    stringData = frame.tobytes()     # type=bytes

    s.sendall((str(len(stringData))).encode().ljust(6) + stringData)
    
cam.release()



'''
cam = cv2.VideoCapture(0)

cam.set(3, 320)
cam.set(4, 240)
 
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
 
while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    # frame을 String 형태로 변환
    data = np.array(frame)
    stringData = data.tostring()
 
    #서버에 데이터 전송 (str(len(stringData))).encode().ljust(16)
    s.sendall((str(len(stringData))).encode().ljust(16) + stringData)
 
cam.release()

'''