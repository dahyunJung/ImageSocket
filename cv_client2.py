import cv2
import socket
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8485))       

cam = cv2.VideoCapture('1215.mp4')
#cam.set(3, 320)
#cam.set(4, 240)

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 10]

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param) 
    data = np.array(frame)  # type=numpy.ndarray print([[255][219][213]], ...)
    stringData = data.tobytes()     # type=bytes

    #서버에 데이터 전송(str(len(stringData))).encode().ljust(16)
    #s.sendall((str(len(stringData))).encode().ljust(6) + stringData)
    s.sendall(stringData)
    print(len(stringData))

cam.release()
