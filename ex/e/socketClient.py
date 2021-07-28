import cv2
import socket
import numpy as np

HOST='127.0.0.1'     # 자신의 컴 ip
PORT=8485

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(2048)
    length = int.from_bytes(data, "big")
    data = s.recv(length)
    sdata = np.fromstring(data, dtype='uint8')
    
    a = cv2.imdecode(data, cv2.IMREAD_COLOR)
    print(a)
    cv2.imshow('d', a)
    cv2.waitKey(1)

    #frame = cv2.imdecode()
