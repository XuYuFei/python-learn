""" 18 - 异常处理及程序调试 """
''' 18.1 - 异常概述 '''
"""
    Python中常见异常：
        - NameError：尝试访问一个没有声明的变量引发的错误；
        - IndexError：索引超出序列范围引发的错误；
        - IndentationError：缩进错误；
        - Value Error：传入的值错误；
        - Key Error：请求一个不存在的字典关键字引发的错误；
        - IOError：输入输出错误（如要读取的文件不存在）；
        - ImportError：当import语句无法找到模块或from无法在模块中找到相应的名称时引发的错误；
        - AttributeError：尝试访问未知的对象属性引发的错误；
        - TypeError：类型不合适引发的错误；
        - MemoryError：内存不足；
        - ZeroDivisionError：除数为0引发的错误；
"""


def division():
    num1 = int(input('请输入被除数：'))
    num2 = int(input('请输入除数：'))
    result = num1 / num2
    print(result)


if __name__ == '__main__':
    division()

''' 18.2 - 异常处理语句 '''
# 18.2.1 - try...except语句
"""
    语法格式：
    try:
        block1
    except [ExceptionName [as alias]]:
        block2
        
    ExceptionName [as alias]：可选参数，用于指定要捕获的异常，不指定异常名称，则表示捕获全部异常
"""


def division():
    num1 = int(input('请输入被除数：'))
    num2 = int(input('请输入除数：'))
    result = num1 / num2
    print(result)


if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print('输入错误：除数不能为0')


# 18.2.2 - try...except...else语句


def division():
    num1 = int(input('请输入被除数：'))
    num2 = int(input('请输入除数：'))
    result = num1 / num2
    print(result)


if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print("\n出错了：除数不能为0")
    except ValueError as e:
        print('输入错误：', e)
    else:
        print('程序执行完成......')

# 18.2.3 - try...except...finally语句
"""
    基本格式：
    try:
        block1
    except [ExceptionName [as alias]]:
        block2
    finally:
        block3
"""


def division():
    num1 = int(input('请输入被除数：'))
    num2 = int(input('请输入除数：'))
    result = num1 / num2
    print(result)


if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print("\n出错了：除数不能为0！")
    except ValueError as e:
        print('输入错误：', e)
    else:
        print('程序执行完成......')
    finally:
        print('资源释放，并关闭')

# 18.2.4 - 使用raise语句抛出异常
"""
    如果某个函数或方法可能会产生异常，但不想在当前函数或方法中处理这个异常，则可以使用raise语句在某个函数或方法中抛出异常；
    raise语句基本格式：raise [ExceptionName[(reason)]
"""


def division():
    num1 = int(input('请输入被除数：'))
    num2 = int(input('请输入除数：'))
    if num2 == 0:
        raise ValueError('除数不能为0')
    result = num1 / num2
    print(result)


if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print("\n出错了：除数不能为0")
    except ValueError as e:
        print('输入错误：', e)

''' 18.3 - 程序调试 '''
# 18.3.1 - 使用自带的IDLE进行程序调试
# 18.3.2 - 使用assert语句调试程序
"""
    assert：断言，一般用于对程序某个时刻必须满足的条件进行验证。
    基本语法：assert expression [,reason]
        - expression：条件表达式，如果该表达式的值为True时，什么都不做；如果为False时，则抛出AssertionError异常；
        - reason：可选参数，用于对判断条件进行描述，为了以后更好地知道哪里出了问题；
"""


def division():
    num1 = int(input('请输入被除数：'))
    num2 = int(input('请输入除数：'))
    assert num2 != 0, "除数不能为0"
    result = num1 / num2
    print(result)


if __name__ == '__main__':
    division()
if __name__ == '__main__':
    try:
        division()
    except AssertionError as e:
        print("\n输入有误：",  e)