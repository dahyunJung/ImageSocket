import cv2
import socket


def getFrame(sec):
    vid.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vid.read()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames


HOST='127.0.0.1'     # 자신의 컴 ip
PORT=8485

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

vid = cv2.VideoCapture('1215.mp4')

sec = 0
frameRate = 1.5 #//it will capture image in each 0.5 second
count = 1
success = getFrame(sec)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

    




#https://medium.com/@iKhushPatel/convert-video-to-images-images-to-video-using-opencv-python-db27a128a481
