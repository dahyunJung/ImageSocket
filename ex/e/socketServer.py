import socket
import time
import cv2

HOST = ''
PORT = 8485

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()     # client연결수
so, ad = s.accept()

try:
    while True:
        cam = cv2.VideoCapture('1215.mp4')

        # frame에는 읽은 frame
        ret, frame = cam.read()
        result, frame = cv2.imencode('.jpg', frame)
        data = frame.tobytes()

        s.sendall(data)
        #time.sleep(0.5)
except:
    print('fin')

finally:
    s.close()