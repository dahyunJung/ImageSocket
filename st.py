import cv2
import socket


def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames


HOST = 'localhost'
PORT = 8585

vid = cv2.VideoCapture('1215.mp4')
res, frame = vid.read()
if res:
    cv2.imwrite(str(count)+'.jpg', frame)

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((HOST, PORT))
serv.listen(5)
conn, addr = serv.accept()
print(addr, '접속')

sec = 0
frameRate = 1.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)


    data = f.read()