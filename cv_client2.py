import cv2
import socket
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8485))       

cam = cv2.VideoCapture(0)
cam.set(3, 320)
cam.set(4, 240)

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame)
    print(type(result))
    print(type(frame))

    data = np.array(frame)
    print(type(data))
    stringData = data.tobytes()
    print(type(stringData))
 
    #서버에 데이터 전송(str(len(stringData))).encode().ljust(16)
    s.sendall((str(len(stringData))).encode().ljust(16) + stringData)
    print(type((str(len(stringData))).encode().ljust(16) + stringData))


cam.release()
