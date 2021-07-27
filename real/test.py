import cv2

cam = cv2.VideoCapture('1215.mp4')
 
while True:
    frame = cam.read()
    #result, frame = cv2.imencode('.jpg', frame)
    #stringData = frame.tobytes()

    #print(len(stringData))
    #print(type(stringData))  #bytes
    #print(stringData)
    
    cv2.imshow('d', frame)
    cv2.waitKey(0)


