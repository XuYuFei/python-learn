""" 13 - 模块 """
''' 13.1 - 模块概述 '''
# 一个扩展名为“.py”的文件就是一个模块

''' 13.2 - 自定义模块 '''
# 13.2.1 - 创建模块
"""
    1.模块名尽量不要与Python自带的标准模块重名；
    2.模块文件扩展名必须是“.py”
"""

# 13.2.2 - 使用import语句导入模块
"""
    基本语法：import moduleName [as alias]
"""
import test
test.getInfo()

# 13.2.3 - 使用from...import语句导入模块
"""
    格式：from modelname import member
"""
from test import getInfo
getInfo()

# 13.2.4 - 模块搜索目录
"""
    import导入模块顺序：
    1.当前目录；
    2.到PYTHONPATH(环境变量)下的每个目录中查找；
    3.到python的默认安装目录下查找；
"""
import sys
print(sys.path)

# 13.2.4 - 1 - 临时添加
# 窗口关闭即失效
import sys
sys.path.append("G:/code/Python/demo2")
print(sys.path)

# 13.2.4 - 2 - 增加.pth文件（推荐）
"""
    例：Lib/site-packages下.pth文件
"""
# 13.2.4 - 3 - 在PYTHONPATH环境变量中添加。

''' 13.3 - 以主程序的形式执行 '''
"""
    模块名称变量：__name__
    顶级模块的__name__变量值为___main__
"""
import demo13 as christmastree
print(christmastree.pinetree)

''' 13.4 - Python中的包 '''
"""
    包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下。
    简单理解就是“文件夹”
    每个包下必须存在一个“__init__.py”的文件
"""
# 13.4.1 - Python程序的包结构
# 13.4.2 - 创建和使用包
# 13.4.2 - 1 - 创建包
"""
    __init__.py中可以不编写代码，该文件中的代码在导入时会自动执行
"""
# 13.4.2 - 2 - 使用包
# 方式一：import+完整包名+模块名
import settings.size
if __name__ == '__main__':
    print('宽度：', settings.size.width)
    print('高度：', settings.size.height)

# 方式二：from + 完整包名 + import + 模块名
from settings import size
if __name__ == '__main__':
    print('宽度：', size.width)
    print('高度：', size.height)

# 方式三：from + 完整包名 + 模块名 + import + 定义名
from settings.size import width, height
if __name__ == '__main__':
    print('宽度：', width)
    print('高度：', height)

''' 13.5 - 引用其他模块 '''
# 13.5.1 - 导入和使用标准模块
# Python 3.8.0 doocument - The Python Language Standard Library
import random
print(random.randint(0, 10))
# 13.5.2 - 第三方模块的下载与安装
"""
    https://pypi.org/
    下载和安装命令：pip <command> [modulename]
    command：install、uninstall、list
    查看安装的第三方模块：pip list    
"""