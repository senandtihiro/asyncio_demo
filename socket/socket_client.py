
'''
socket

connect()

send()

recv()

close()

'''
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8001))

# client.send('bobby'.encode('utf8'))
# data = client.recv(1024)
# print('接收到来自server的数据:', data.decode('utf8'))
# client.close()

while True:
    re_data = input()
    client.send(re_data.encode('utf8'))
    data = client.recv(1024)
    print('接收到来自server的数据:', data.decode('utf8'))
