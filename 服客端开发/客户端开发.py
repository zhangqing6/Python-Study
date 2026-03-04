import socket
socket_client = socket.socket()
socket_client.connect(('localhost', 1144))
while True:
    msg=input("请输入要给服务端发送的消息：")
    if msg=='exit':
        break
    socket_client.send(msg.encode('UTF-8'))
    recv_data = socket_client.recv(1024)
    print(f"服务端回复的消息是{recv_data.decode('UTF-8')}")

socket_client.close()