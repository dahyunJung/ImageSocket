import socket

# 소켓 생성하기
s = socket.socket()

port = 80
s.bind(('127.0.0.1', port))
s.listen(5)

while True:
    # client의 소켓과 주소를 기다리기
    c, addr = s.accept()
    print('클라이언트 주소는 : ', addr)

    # 클라이언트에게 답장보내기
    c.send('안녕 난 서버야'.encode())

# 소켓 닫기
c.close()