# *_* code: UTF-8 *_*
# author:   Beiyu
# datetime: 2019-12-22 16:25
# filename: learn-17-client3.PY
# tool:     PyCharm
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('已连接')
data = input('请输入要转换的温度（单位：摄氏温度）：')
address = ('127.0.0.1', 8888)
temp = s.sendto(data.encode(), address)
print('发送的字节数：' + str(temp))

data, addr = s.recvfrom(1024)
print(str(data.decode()))
# print('返回华氏温度为：' + data, '地址为：' + addr)

s.close()