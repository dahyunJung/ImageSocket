import cv2

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

cam = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)