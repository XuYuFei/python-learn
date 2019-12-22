# *_* code: UTF-8 *_*
# author:   Beiyu
# datetime: 2019-12-22 11:43
# filename: learn-17.PY
# tool:     PyCharm

""" 17 - 网络编程
    网络编程就是如何在程序中实现两台计算机的通信。
    基础知识：TCP协议、UDP协议，以及如何使用TCP编程、UDP编程
"""

''' 17.1 - 网络基础 '''
# 17.1.1 - 为什么要使用通信协议
"""
    目的：连接所有厂商不同类型的电脑
    互联网协议簇：Internet Protocol suite，即通用协议标准
"""

# 17.1.2 - TCP/IP简介
"""
    1.IP协议
    互联网上每个计算机的唯一标识就是IP地址。
    IP地址实际上是一个32位的整数（IPv4）。
    IP协议负责把数据从一台计算机通过网络发送到另一台计算机。
    2.TCP协议
        - TCP协议是建立在IP协议之上的。
        - TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。
        - TCP协议会通过3次握手建立可靠连接，然后需要对每个IP包进行编号，确保对方按顺序收到，如果包丢了，就自动重发。
"""

# 17.1.3 - UDP简介
"""
    相对TCP协议，UDP协议则是面向无连接的协议。
    使用UDP协议，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发送数据包。
"""

# 17.1.4 - Socket简介
"""
    Socket：
        - 英文原意是“孔”或“插座”，通常也称作“套接字”，用于描述IP地址和端口；
        - 它是一个通信链的句柄，可以用来实现不同虚拟机或不同计算机间的通信；
    Python中使用socket模块的socket()函数完成，语法格式：
        - s = socket.socket(AddressFamily, Type)
            - AddressFamily：可以选择AF_INET（用于Internet进程间通信），或AF_UNIX（用于同一台机器进程间通信）；
            - Type：套接字类型，可以是SOCK_STREAM（流式套接字，主要用于TCP协议），或SOCK_DGRAM（数据报套接字，主要用于UDP协议）；
    
    示例：
        创建TCP/IP套接字：
            - tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        创建UDP/IP套接字：
            - udpSock = socket.socket(socket.AF_INEt, socket.SOCK_DGRAM)
                
    创建完成后，生成一个socket对象，主要方法如下：
        - s.bind()：绑定地址（host, port）到套接字，在AF_INET下，以元组(host, port)的形式表示地址；
        - s.listen()：开始TCP监听；backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量，该值至少为1，大部分应用程序设为5即可；
        - s.accept()：被动接受TCP客户端连接（阻塞式），等待连接的到来；
        - s.connect()：主动初始化TCP服务器连接，一般address的格式为元组（hostname, port）,如果连接出错，则返回socket.error错误；
        - s.recv()：接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略；
        - s.send()：发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小；
        - s.sendall()：完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常；
        - s.recvfrom()：接收UDP数据，与recv()类似，但返回值是（data, address）.
            - data：包含接收数据的字符串；
            - address：发送数据的套接字地址
        - s.sendto()：发送UDP数据，将数据发送到套接字，address形式为（ipaddr, port）的元组，指定远程地址。返回值是发送的字节数；
        - s.close()：关闭套接字；
"""


''' 17.2 - TCP编程 '''
"""
    由于TCP连接具有安全可靠的特性，所以TCP引用更为广泛。
    客户端：主动发起连接的
    服务端：被动响应连接的
"""

# 17.2.1 - 创建TCP服务器
"""
    流程：
        - 使用socket()创建一个套接字
        - 使用bind()绑定IP和port
        - 使用listen()使套接字变为可被动连接
        - 使用accept()等待客户端连接
        - 使用recv/send()接收发送数据
"""
# 例如：使用socket模块，通过客户端浏览器向本地服务器发起请求，服务器接收到请求，向浏览器发送“hello world”。
"""
import socket                                                    # 导入socket模块
host = '127.0.0.1'                                               # 主机IP
port = 8080                                                      # 端口号
web = socket.socket()                                            # 创建socket对象
web.bind((host, port))                                           # 绑定端口
web.listen(5)                                                    # 设置最多连接数
print('服务器等待客户端连接......')

while True:
    conn, addr = web.accept()                                    # 建立客户端连接
    data = conn.recv(1024)                                       # 获取客户端请求数据
    print(data)
    conn.sendall(b"HTTP/1.1 200 OK\r\n\r\nHello World")          # 向客户端发送数据
    conn.close()                                                 # 关闭连接
"""

# 17.2.2 - 创建TCP客户端

"""
    见：
        - learn-17-server2.py
        - learn-17-client2.py 
"""


''' 17.3 - UDP编程 '''
"""
    UDP是面向消息的协议，如果通信时不需要建立连接，数据的传输自然是不可靠的，UDP一般用于多点通信和实时的数据业务；
    例如：
        - 语音广播
        - 聊天软件
        - TFTP（简单文件传送）
        - SNMP（简单网络管理协议）
        - RIP（路由信息协议，如报告股票市场、航空信息）
        - DNS（域名解析）
"""

# 17.3.1 - 创建UDP服务器
# 17.3.2 - 创建UDP客户端
"""
    创建一个UDP客户端步骤：
        - 创建客户端套接字
        - 发送/接收数据
        - 关闭套接字
    
    接收和发送的数据都是byte。因此发送时使用encode()将字符串转化为byte；接收时使用decode()将byte转换为字符串；
    
    示例见：
        - learn-17-server3.py
        - learn-17-client3.py
"""






















