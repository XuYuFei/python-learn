""" 12 - 类和对象 """
''' 12.1 - 面向对象概述 '''
# 12.1.1 - 对象
# 12.1.2 - 类
# 12.1.3 - 面向对象程序设计的特点
# 封装
# 继承
# 多态

''' 12.2 - 类的定义和使用 '''


# 12.2.1 - 定义类
# class ClassName:
#       ''' 类的帮助信息 ''' # 类文档字符串
#       statement           # 类体
class Geese:
    '''大雁类'''
    pass


# 12.2.2 - 创建类的实例
# ClassName(parameterlist)
wildGoose = Geese()
print(wildGoose)


# 12.2.3 魔术方法 - __init__()
class Geese:
    """大雁类"""

    def __init__(self):
        print('我的大雁类！')


wildGoose = Geese()


class Geese:
    """大雁类"""

    def __init__(self, beak, wing, claw):
        print('我的大雁类！我有以下特征：')
        print(beak)
        print(wing)
        print(claw)


beak = 'beak'
wing = 'wing'
claw = 'claw'
wildGoose = Geese(beak, wing, claw)

# 12.2.4 - 创建类的成员并访问
# 12.2.4 - 1.创建实例方法并访问
"""
    实例方法：第一个参数必须是self
    格式：
    def functionName(self, parameterlist):
        block
        
    访问：
    instanceName.functionName(parametervalue)
"""


# 12.2.4 - 2.创建数据成员并访问
# 类属性


class Geese:
    """大雁类"""
    neck = '脖子长'
    wing = '振翅频率高'
    leg = '两条腿'

    def __init__(self):
        print('我是大雁，我有以下特性：')
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)


geese = Geese()


# 实例属性
# 实例属性是指定义在类的方法中的属性，只作用于当前实例中


class Geese:
    """大雁类"""

    def __init__(self):
        self.neck = '脖子长'
        self.wing = '振翅频率高'
        self.leg = '两条腿'
        print('我是大雁，我有以下特性')
        print(self.neck)
        print(self.wing)
        print(self.leg)


geese == Geese()


class Geese:
    def __init__(self):
        self.neck = '脖子较长'
        print(self.neck)


goose1 = Geese()
goose2 = Geese()
goose1.neck = '脖子没有天鹅的长'
print(goose1.neck)
print(goose2.neck)

# 12.2.5 - 访问限制
"""
    __foo__：首尾下划线表示定义特殊方法，一般是系统定义名字，如__init__()
    _foo：protected类型，只允许类本身和子类进行访问，不能使用"from module import * "语句导入
    __foo：private类型，只允许定义该方法的类本身访问，不能通过类的实例进行发访问
        可以通过“类的实例名.类名__xxx”方式访问
"""


class Animal:
    """动物类"""
    _name = '动物'

    def __init__(self):
        print('__init__()：', Animal._name)


dog = Animal()
print('直接访问：', dog._name)


class Animal:
    """动物类"""
    __name = '动物'

    def __init__(self):
        print("__init__()；", Animal.__name)


dog = Animal()
print("加入类名：", dog._Animal__name)

''' 12.3 - 属性 '''
# 12.3.1 创建用于计算的属性
"""
    通过@property(装饰器)将一个方法转换为属性，从而实现用于计算的属性
    @property
    def methodname(self):
        block
"""


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rect = Rect(100, 200)
print('面积为：', rect.area)


# 12.3.2 - 为属性添加安全保护机制


class TVshow:
    def __init__(self, show):
        self.__show = show

    @property
    def show(self):
        return self.__show


tvshow = TVshow('正在播放：《海贼王》')
print(tvshow.show)

''' 12.4 - 继承 '''
# 12.4.1 - 继承的基本语法
"""
    class ClassName(baseClassList):
        statement
"""


# 12.4.2 - 方法重写


class Fruit:
    color = '绿色'

    def harvest(self, color):
        print(Fruit.color)


class Orange(Fruit):
    color = '橙色'

    def __init__(self):
        print('我是橘子')

    def harvest(self, color):
        print(Orange.color)

# 12.4.3 - 派生类中调用基类的__init__()方法


class Fruit:
    def __init__(self, color = '绿色'):
        Fruit.color = color

    def harvest(self):
        print('水果原来是：' + Fruit.color + '的！')


class Apple(Fruit):
    def __init__(self):
        super().__init__()
        print('我是苹果')


apple = Apple()
apple.harvest()