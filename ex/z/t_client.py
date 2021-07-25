import socket

HOST = '192.168.219.115'  # 로컬은 127.0.0.1의 ip로 접속한다.
PORT = 9101         # port는 위 서버에서 설정한 9999로 접속을 한다.

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 소켓을 만든다.
client_socket.connect((HOST, PORT))     # connect함수로 접속을 한다.


for i in range(1, 10):      # 10번의 루프로 send receive를 한다.
    msg = 'hello'       # 메시지는 hello로 보낸다.
    data = msg.encode()     # 메시지를 바이너리(byte)형식으로 변환한다.
    length = len(data)      # 메시지 길이를 구한다.
    client_socket.sendall(length.to_bytes(4, byteorder="little"))    # server로 리틀 엔디언 형식으로 데이터 길이를 전송한다.
    client_socket.sendall(data)     # 데이터를 전송한다.
    data = client_socket.recv(4)    # server로 부터 전송받을 데이터 길이를 받는다.
    length = int.from_bytes(data, "little")     # 데이터 길이는 리틀 엔디언 형식으로 int를 변환한다.
    data = client_socket.recv(length)   # 데이터 길이를 받는다.
    msg = data.decode()     # 데이터를 수신한다.
    print('Received from : ', msg)      # 데이터를 출력한다.

client_socket.close()


# 출처: https://nowonbun.tistory.com/668 [명월 일지]