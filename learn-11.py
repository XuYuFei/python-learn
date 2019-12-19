""" 11 - 用函数实现模块化程序设计 """
''' 11.1 - 函数 的创建和调用 '''


# 11.1.1 - 创建一个函数
# def functionname([parameterlist]):
#   ['''comments''']
#   [functionbody]

def filterchar(string):
    """功能：过滤字符串
        string：要过滤的字符串
        """
    import re
    pattern = r'(hello)|(world)'
    sub = re.sub(pattern, '@_@', string)
    print(sub)


# 11.1.2 -- 调用函数
# functionname([parametersvalue])
str = 'hello world python java'
filterchar(str)

# 11.1.3 - 空语句
def func():
    ...


''' 11.2 - 参数传递 '''
# 11.2.1 - 形式参数和实际参数
# 11.2.1 - 1 通过作用理解
# 当实参为不可变对象时，进行的是值传递；【进行值传递后，改变形参的值，实参的值不变】
# 当实参为可变对象时，进行的时引用传递【进行引用传递后，改变形参的值，实参的值也一同改变】
def demo(obj):
    print("原值：", obj)
    obj += obj


# 调用函数
print('==========值传递==========')
str = 'hello world'
print('函数调用前：', str)
demo(str)
print('函数调用后：', str)
print('=========引用传递========')
list1 = ['hello', 'world']
print('函数调用前：', list1)
demo(list1)
print('函数调用后：', list1)

# 11.2.2 - 位置参数
# 11.2.2 - 1 数量必须与定义时一致
# 11.2.2 - 2 位置必须与定义时一致

# 11.2.3 - 关键字参数
def person(name, weight, height):
    print('姓名：' + name, '体重：' + weight, '身高：' + height)


person('小明', '60KG', '180')
person(weight = '80KG', height = '180', name = '小红')

# 11.2.4 - 为参数设置默认值
def demo(obj = []):
    print('obj的值：', obj)
    obj.append(1)


demo()
demo()
demo()

def demo(obj = None):
    if obj == None:
        obj = []
    print('obj的值：', obj)
    obj.append(1)


demo()
demo()

# 11.2.5 - 可变参数
# *parameter 表示接收任意多个实际参数放到一个元组中
def demo1(*param):
    print('*param：', *param)
    print('param：', param)
    for item in param:
        print(item)
demo1('hello', 'world', 'python')
demo1(*['hello', 'world'])

# **parameter 表示接收任意多个显式赋值参数，并将其放到一个字典中
def demo2(**param):
    print()
    for key, value in param.items():
        print(key + "的爱好是：" + value)
demo2(小明 = '钢琴', 小红 = '唱歌')
demo2(**{ '小明': '钢琴', '小红': '唱歌' })

''' 11.3 - 返回值 '''
def getHobby(name = None):
    hobby = ''
    if name == 'Lucy':
        hobby = 'Song'
    else:
        hobby = 'Swim'
    return hobby
hobby = getHobby()
print(hobby)
hobby = getHobby('Lucy')
print(hobby)

''' 11.4 - 变量的作用域 '''
# 11.4.1 - 局部变量
# 11.4.2 - 全局变量

''' 11.5 - 匿名函数 '''
# result = lambda [arg1 [, arg2, ..., argn]]:expression
import math
def get_circle_area(r):
    result = math.pi * r * r
    return result
r = 10
print('半径为', r, '的圆面积为：', get_circle_area(r))

result = lambda r:math.pi * r * r
print('半径为', r, '的圆面积为：', result(r))


