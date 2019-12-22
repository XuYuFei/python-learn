""" 16 - 进程和线程 """
''' 16.1 - 什么是进程 '''
# 进程是计算机中已运行程序的实体。

''' 16.2 - 创建进程的常用方式 '''
# 16.2.1 - 使用multiprocessing模块创建进程
"""
    multiprocessing提供了一个Process类来代表一个进程对象。
    语法：Process([group [, target [, name [, args [, kwargs]]]]])
    参数：
        - group：未使用，始终为None
        - target：表示当前进程启动时执行的可调用对象
        - name：当前进程实例的别名
        - args：传递给target函数的元组
        - kwargs：传递给target函数的参数字典 
"""
from multiprocessing import Process  # 导入模块


# 执行子进程
def test(interval):
    print('我是子进程')


# 执行主进程
def main():
    print('我是主进程')
    p = Process(target=test, args=(1,))  # 实例化Process进程类
    p.start()
    print('主进程结束')


if __name__ == '__main__':
    main()

"""
    Process实例p常用方法：
        - is_alive()：判断进程实例是否还在执行
        - join([timeout])：是否等待进程实例执行结束，或等待多少秒
        - start()：启动进程实例（创建子进程）
        - run()：target参数不存在，调用start()方法时，执行对象中的run()方法
        - terminate()：不管任务是否完成，立即终止
        常用属性：
        - name：进程实例别名
        - pid：当前实例的PID值
"""
from multiprocessing import Process
import time
import os


# 两个子进程将会调用的方法
def child_1(interval):
    print("子进程（%s）开始执行，父进程为（%s）" % (os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("子进程（%s）执行时间为'%0.2f'秒" % (os.getpid(), t_end - t_start))


def child_2(interval):
    print("子进程（%s）开始执行，父进程为（%s）" % (os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("子进程（%s）执行时间为'%0.2f'秒" % (os.getpid(), t_end - t_start))


if __name__ == '__main__':
    print('-' * 10, '父进程开始执行', '-' * 10)
    print("父进程PID：%s" % os.getpid())
    p1 = Process(target=child_1, args=(1,))
    p2 = Process(target=child_2, args=(2,), name='hello')
    p1.start()
    p2.start()
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
    print("p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)
    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)
    print("-" * 5, '等待子进程', '-' * 5)
    p1.join()
    p2.join()
    print('-' * 10, '父进程执行结束', '-' * 10)

# 16.2.2 - 使用Process子类创建进程
from multiprocessing import Process
import time
import os


# 继承Process
class SubProcess(Process):
    def __init__(self, interval, name=''):
        Process.__init__(self)
        self.interval = interval
        if name:
            self.name = name

    # 重写Process类run()方法
    def run(self):
        print("子进程（%s）开始执行，父进程为（%s）" % (os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_end = time.time()
        print("子进程（%s）执行结束，耗时%0.2f秒" % (os.getpid(), t_end - t_start))


if __name__ == '__main__':
    print("-" * 15, "父进程开始执行", "-" * 15)
    print("父进程PID：%s" % os.getpid())
    p1 = SubProcess(interval=1, name='hello')
    p2 = SubProcess(interval=2)
    # 对于一个不包含target属性的Process类执行start()方法，就会运行这个类中的run()方法
    p1.start()
    p2.start()
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
    print("p1.name = %s" % p1.name)
    print("p1.pid = %s" % p1.pid)
    print("p2.name = %s" % p2.name)
    print("p2.pid = %s" % p2.pid)
    print("-" * 5, "等待子进程", "-" * 5)
    p1.join()
    p2.join()
    print("-" * 15, "父进程结束", "-" * 15)

# 16.2.3 - 使用进程池Pool创建进程
"""
    Pool类常用方法：
        - apply_async(func[, args[, kwds]])：使用非阻塞方式调用func()函数（并行执行，阻塞方式必须等待上一个进程退出才能执行下一个进程）
        - apply(func[, args[, kwds]])：使用阻塞方式调用func()函数
        - close()：关闭Pool，使其不再接受新的任务
        - terminate()：不管任务是否完成，立即终止
        - join()：主进程阻塞，等待子进程的退出，必须在close或terminate后使用
"""
from multiprocessing import Pool
import time, os


def task(name):
    print("子进程（%s）执行task %s..." % (os.getpid(), name))
    time.sleep(1)


if __name__ == '__main__':
    print('父进程（%s）。' % os.getpid())
    p = Pool(3)  # 定义一个进程池，最大进程数3
    for i in range(10):  # 从0开始循环10次
        p.apply_async(task, args=(i,))  # 使用非阻塞方式调用task()函数
    print("等待所有子进程结束......")
    p.close()  # 关闭进程池，关闭后p不再接收新的请求
    p.join()  # 等待子进程结束
    print('所有子进程结束。')

''' 16.3 - 通过队列实现进程间通信 '''
from multiprocessing import Process


def plus():
    print('-' * 10, '子进程1开始', '-' * 10)
    global g_num
    g_num += 50
    print('g_num is %d' % g_num)
    print('-' * 10, '子进程1结束', '-' * 10)


def minus():
    print('-' * 10, '子进程2开始', '-' * 10)
    global g_num
    g_num -= 50
    print('g_num is %d' % g_num)
    print('-' * 10, '子进程2结束', '-' * 10)


g_num = 100

if __name__ == '__main__':
    print('-' * 10, '主进程开始', '-' * 10)
    print('g_num is %d' % g_num)
    p1 = Process(target=plus)
    p2 = Process(target=minus)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('-' * 10, '主进程结束', '-' * 10)

# 16.3.1 - 队列简介
"""
    队列（Queue）就是模仿现实中的排队。
    队列两个特点：
        - 新来的排在队尾
        - 最前面的完成后离队，后面一个跟上
"""

# 16.3.2 - 多进程队列的使用
"""
    Queue常用方法：
    - Queue.qsize：返回当前队列包含的消息数量；
    - Queue.empty()：如果消息队列为空，返回True；反之返回False；
    - Queue.full()：如果队列满了，返回True；反之返回False；
    - Queue.get(block[, timeout])：获取队列中的一条消息，然后将其从队列中移除;block默认值为True;
        -- 若block=True，且没有设置timeout，消息队列为空，此时程序将被阻塞（停在读取状态），直到从消息队列读到消息为止；
           如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出"Queue.Empty"异常。
        -- 若block=False，消息队列为空，则会立即抛出"Queue.Empty"异常。
    - Queue.get_nowait()：相当于Queue.get(False)
    - Queue.put(item, [block [, timeout]])：将消息写入队列，block默认值为True;
        -- 若block=True，且没有设置timeout，消息队列如果已经没有空间可写入，此时程序将被阻塞（停在写入状态），直到从消息队列腾出空间为止；
           如果设置了timeout，则会等待timeout秒，若还没有空间，则抛出"Queue.Full"异常；
        -- 若block=Flase,消息队列没有空间可写入，则会立即抛出"Queue.Full"异常；
    - Queue.put_nowait(item)：相当于Queue.put(item, false)
"""
from multiprocessing import Queue

if __name__ == '__main__':
    print('*' * 15, '多进程队列的使用', '*' * 15)
    q = Queue(3)
    q.put('消息1')
    q.put('消息2')
    print(q.full())
    q.put('消息3')
    print(q.full())

    try:
        q.put('消息4', True, 2)
    except:
        print('消息队列已满，现有消息数量：%s' % q.qsize())

    try:
        q.put_nowait('消息4')
    except:
        print('消息队列已满，现有消息数量：%s' % q.qsize())

    if not q.empty():
        print('从队列中读取消息')
        for i in range(q.qsize()):
            print(q.get_nowait())
    if not q.full():
        q.put_nowait('消息4')

# 16.3.3 - 使用队列在进程间通信
from multiprocessing import Process, Queue
import time


def write_task(q):
    if not q.full():
        for i in range(5):
            message = '消息' + str(i)
            q.put(message)
            print('写入：%s' % message)


def read_task(q):
    time.sleep(1)
    while not q.empty():
        print('读取：%s' % q.get(True, 2))


if __name__ == '__main__':
    print('*' * 10, '父进程开始', '*' * 10)
    q = Queue()
    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()

''' 16.4 什么是线程 '''
"""
    线程（Thread）:
        - 是操作系统能够进行运算调度的最小单位；
        - 它被包含在进程中，是进程中的实际运作单位；
        - 一条线程指的是进程中一个单一顺序的控制流，一个进程中多以并发多个线程，每条线程执行不同的任务；
"""
''' 16.5 - 创建线程 '''
"""
    Python标准库提供两个模块：_thread - 低级模块、threading - 高级模块
"""

# 16.5.1 - 使用threading模块创建线程
"""
    threading模块提供了一个Thread类来代表一个线程对象
    Thread语法格式：
        - Thread([group [, target [, name [, args [, kwargs]]]]])
    参数说明：
        - group：None，为以后版本保留
        - target：表示一个可调用对象，线程启动时，run()方法将调用此对象，默认为None，表示不调用任何内容
        - name：当前线程名称，默认创建一个“Thread-N”格式的唯一名称
        - args：传递给target()函数的参数元组
        - kwargs：传递给target()函数的参数字典
"""
import threading, time


def process():
    for i in range(3):
        time.sleep(1)
        print('thread name is %s' % threading.current_thread().name)


if __name__ == '__main__':
    print('*' * 20, '16.5.1 - 主线程开始', '*' * 20)
    threads = [threading.Thread(target=process) for i in range(4)]  # 创建4个线程，存入列表
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('*' * 20, '16.5.1 - 主线程结束', '*' * 20)

# 16.5.2 - 使用Thread子类创建线程
import threading, time


class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = '子线程' + self.name + '执行，i=' + str(i)  # name属性中保存当前线程的名字
            print(msg)


if __name__ == '__main__':
    print('*' * 20, '16.5.2 - 主线程开始', '*' * 20)
    t1 = SubThread()
    t2 = SubThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('*' * 20, '16.5.2 - 主线程结束', '*' * 20)


def hr(sign, number, string):
    print(sign * number, string, sign * number)


''' 16.6 - 线程间通信 '''
"""
    在一个进程内的所有线程共享全局变量，能够在不使用其他方式的前提下完成多线程之间的数据共享
"""
from threading import Thread
import time


def plus():
    hr('*', 15, '子线程1开始')
    global g_num
    g_num += 50
    print('g_num is %d' % g_num)
    hr('*', 15, '子线程1结束')


def minus():
    time.sleep(1)
    hr('*', 15, '子线程2开始')
    global g_num
    g_num -= 50
    print('g_num is %d' % g_num)
    hr('*', 15, '子线程2结束')


g_num = 100
if __name__ == '__main__':
    hr('*', 20, '16.6 - 主线程开始')
    print('g_num is %d' % g_num)
    t1 = Thread(target=plus)
    t2 = Thread(target=minus)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    hr('*', 20, '16.6 - 主线程结束')

# 16.6.1 - 什么是互斥锁
"""
    互斥锁（Mutual exclusion:Mutex）：防止多个进程同时读写某一块内存区域。
    状态：锁定、非锁定
"""
# 16.6.2 - 使用互斥锁
"""
    threading模块中使用Lock类处理锁定
    Lock类方法：
        - acquire()：获取锁定，如果有必要，需要阻塞到锁定释放为止。
        - release()：释放锁
    示例：
        mutex = threading.Lock()   # 创建锁
        mutex.acquire([blocking])  # 锁定
        mutex.release()            # 释放锁
"""
from threading import Thread, Lock
import time

n = 100


def task():
    global n
    mutex.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    print('购买成功，剩余%d张电影票' % n)
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    t_l = []
    for i in range(10):
        t = Thread(target=task)
        t_l.append(t)
        t.start()
    for t in t_l:
        t.join()

# 16.6.3 - 使用队列在线程间通信
"""
    队列在线程间通信：使用queue模块的Queue队列
    使用Queue线程间通信通常应用于生产者消费者模式
"""
from queue import Queue
import random, threading, time


# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            print('生产者%s将产品%d加入队列！' % (self.getName(), i))
            self.data.put(i)
            time.sleep(random.random())
        print('生产者%s完成！' % self.getName())


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print('消费者%s将产品%d从队列中取出！' % (self.getName(), val))
            time.sleep(random.random())
        print('消费者%s完成！' % self.getName())


if __name__ == '__main__':
    hr('*', 30, '16.6.3 - 主线程开始')
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    hr('*', 30, '16.6.3 - 主线程结束')

''' 16.7 - 关于线程需要注意的两点 '''
"""
    # 16.7.1 - 进程和线程的区别
    - 进程是系统进行资源分配和调度的一个独立单位，线程是进程的一个实体，是CPU调度和分派的基本单位；
    - 进程之间是相互独立的，多进程中，同一个变量，各自有一份备份存在于每个进程中，但互不影响；
      而同一个进程的多个线程是内存共享的，所有变量都由所有线程共享；
    - 由于进程间是独立的，因此一个进程的崩坏不会影响其他的进程；
      而线程是包含在进程之内的，线程的崩溃就会引发进程的崩溃，继而导致同一进程内的其他线程的崩溃。
"""