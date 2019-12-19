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
from multiprocessing import Process # 导入模块

# 执行子进程
def test(interval):
    print('我是子进程')

# 执行主进程
def main():
    print('我是主进程')
    p = Process(target = test, args = (1,)) # 实例化Process进程类
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