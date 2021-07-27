# Jetson Nano 카메라 영상 보내주는 https://blog.daum.net/ejleep1/1006
import cv2
import socket
import numpy as np

# jetson nano camera
def gstreamer_pipeline(
    capture_width=3280, capture_height=2464,
    display_width=640, display_height=480,
    framerate=21, flip_method=2,      # 추후 화면방향에 맞게 바꾸기
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width, capture_height,
            framerate, flip_method,
            display_width, display_height,
        )
    )


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   ## TCP 사용
s.connect(('192.168.219.193', 8485))    ## server ip, port

cam = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER) 
while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame)
    data = np.array(frame)
    stringData = data.tostring()
 
    s.sendall((str(len(stringData))).encode().ljust(16) + stringData)
 
cam.release()
