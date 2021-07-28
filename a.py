import cv2
import socket
 
HOST = '127.0.0.1'
PORT = 8585


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

## webcam 이미지 capture
cam = cv2.VideoCapture('1215.mp4') 
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
 
while True:
    ret, frame = cam.read()

    # frame을 jpg로 이미지를 인코딩한다.
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    stringData = frame.tobytes()

    #print(stringData) # /x42
    
    s.sendall((str(len(stringData))).encode().ljust(16) + stringData)

cam.release()
