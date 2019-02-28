'''
socket

bind(协议，地址，端口)

listen(监听客户端socket请求)

accept()

recv()

send()

close()
'''
import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8001))
server.listen()
# sock, addr = server.accept()

# 获取从客户端发送的数据
# 一次获取1K的数据
# data = sock.recv(1024)
# print(data.decode('utf8'))
# # send的是client发送过来的数据，所以要先解码，
# # 而发送出去的时候要求是二进制数据，因此要再进行编码
# sock.send('hello {}'.format(data.decode('utf8')).encode('utf8'))
# server.close()
# sock.close()


def handle_sock(sock, addr):
    '''
    用于接收用户的输入，同时发送新的消息给client
    :param sock:
    :param addr:
    :return:
    '''
    data = sock.recv(1024)
    print('接收到来自client的数据：', data.decode('utf8'))
    re_data = input()
    sock.send(re_data.encode('utf8'))


# 在此基础上实现初级的聊天功能
while True:
    sock, addr = server.accept()
    # 用线程去处理新接收的连接（用户）
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
