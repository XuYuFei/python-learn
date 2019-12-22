# *_* code: UTF-8 *_*
# author:   Beiyu
# datetime: 2019-12-22 16:24
# filename: learn-17-server3.PY
# tool:     PyCharm
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))
print('绑定UDP到8888端口')
data, addr = s.recvfrom(1024)
data = float(data) * 1.8 + 32
send_data = '转换后的温度（单位：华氏温度）：' + str(data)
print('Received from %s:%s' % addr)
s.sendto(send_data.encode(), addr)
s.close()
