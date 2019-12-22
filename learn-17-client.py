# *_* code: UTF-8 *_*
# author:   Beiyu
# datetime: 2019-12-22 15:42
# filename: learn-17-client.PY
# tool:     PyCharm
import socket
s = socket.socket()                         # 创建TCP/IP套接字
host = '127.0.0.1'                          # 获取主机地址
port = 8080                                 # 设置端口号
s.connect((host, port))                     # 主动初始化TCP服务器连接
send_data = input('请输入要发送的数据：')
s.send(send_data.encode())                  # 发送TCP数据
recvData = s.recv(1024).decode()
print('接收到的数据为：', recvData)
s.close()