import cv2
import numpy as np

cam = cv2.VideoCapture('1215.mp4')

ret, frame = cam.read()

# frame을 jpg로 이미지를 인코딩한다.
while True:
    result, frame = cv2.imencode('.jpg', frame)
    cv2.imshow('s', frame)
    #cv2.waitKey(1)