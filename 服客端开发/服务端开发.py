import socket
# 创建Socket对象
socket_server=socket.socket()
# 绑定ip地址及端口
socket_server.bind(('localhost',1144))
# 监听端口
socket_server.listen(1)
# 等待客户端连接
# result:tuple=socket_server.accept()
# conn=result[0]     # 客户端和服务端的连接对象
# address=result[1]  # 客户端地址信息
conn,address=socket_server.accept()
print(f"接收到了客户端的连接，客户端的信息:{address}")
while True:
    data:str=conn.recv(1024).decode('utf-8')
    # recv接受的是缓冲区大小，然后将字节数组转换为字符串
    print(f"客户端发来的消息：{data}")
    msg=input("请输入你要和客户端回复的消息：")
    if(msg=="exit"):
        break
    conn.send(msg.encode('utf-8'))
conn.close()
socket_server.close()