import socket
import cv2

HOST = '127.0.0.1'	
PORT = 8485

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
client_socket.connect((HOST, PORT))	

# 메시지를 보낸다.	
msg = 'java hello'
# 메시지를 바이너리(byte)형식으로 변환	
data = msg.encode()	
# 메시지 길이를 구한다.	
length = len(data)	
# server로 little 엔디언 형식으로 데이터 길이를 전송한다.	
#client_socket.sendall(length.to_bytes(4, byteorder="little"))	
# 데이터를 전송한다.	
client_socket.sendall(data)
 	
client_socket.close()


# 출처: https://nowonbun.tistory.com/672 [명월 일지]