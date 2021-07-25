import socket
import threading

# binder함수: 서버에서 accept 되면 생성되는 socket를 통해 client로부터 데이터 받으면 echo형태로 재송신
def binder(client_socket, addr):
    print('Connected by', addr)     # 커넥션이 되면 접속 주소가 나온다.

    try:    # 접속 상태에서는 client로 부터 받을 데이터를 무한 대기, 만약 접속이 끊기게 된다면 except가 발생해서 접속이 끊기게 된다.
        while True:
            data = client_socket.recv(4)    # socket의 recv함수는 연결된 소켓으로부터 데이터를 받을 대기하는 함수, 최초 4바이트를 대기
            # 최초 4바이트는 전송할 데이터의 크기. 크기는 little big 엔디언으로 byte에서 int형식으로 변환한다.
            length = int.from_bytes(data, "little")
            data = client_socket.recv(length) # 다시 데이터를 수신
            msg = data.decode() # 수신된 데이터를 str형식으로 decode
            print('Received from', addr, msg)   # 수신된 메시지를 콘솔에 출력
            msg = "echo : " + msg       # 수신된 메시지 앞에 「echo:」 라는 메시지
            data = msg.encode()     # 바이너리(byte)형식으로 변환
            length = len(data)      # 바이너리의 데이터 사이즈를 구한다.
            client_socket.sendall(length.to_bytes(4, byteorder='little'))     # 데이터 사이즈를 little 엔디언 형식으로 byte로 변환한 다음 전송
            client_socket.sendall(data)     # 데이터를 클라이언트로 전송
    except:     # 접속이 끊기면 except가 발생
        print("except : " , addr)
    finally:    # 접속이 끊기면 socket 리소스를 닫는다.
        client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     # 소켓 레벨과 데이터 형태를 설정
server_socket.bind(('', 9999))      # 빈port는 cmd에서 netstat -an | find "LISTEN"으로 확인가능
server_socket.listen()      # server 설정이 완료시, listen를 시작

try:    # 서버는 여러 클라이언트를 상대하기 때문에 무한 루프를 사용
    while True:
        client_socket, addr = server_socket.accept()        # client로 접속이 발생하면 accept가 발생, client 소켓과 addr(주소)를 튜플로 받는다.
        th = threading.Thread(target=binder, args = (client_socket,addr))       # 쓰레드 이용해서 client 접속 대기, accept로 넘어가서 다른 client 대기
        th.start()
except:
    print("server")
finally:
    server_socket.close()  # 에러가 발생하면 서버 소켓을 닫는다.


# 출처: https://nowonbun.tistory.com/672