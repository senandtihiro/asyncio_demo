'''
socket

bind(协议，地址，端口)

listen(监听客户端socket请求)

accept()

recv()

send()

close()
'''

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()
sock, addr = server.accept()

# 获取从客户端发送的数据
# 一次获取1K的数据
data = sock.recv(1024)
print(data.decode('utf8'))
# send的是client发送过来的数据，所以要先解码，
# 而发送出去的时候要求是二进制数据，因此要再进行编码
sock.send('hello {}'.format(data.decode('utf8')).encode('utf8'))
server.close()
sock.close()