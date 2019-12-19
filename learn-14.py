""" 14 - 文件与IO """
''' 14.1 - 基本文件操作 '''
# 14.1.1 - 创建和打开文件
"""
    操作文件：
        先创建或者打开指定文件；
        创建文件对象；
    open函数语法格式：
        file = open(filename[, mode[, buffering]])
        mode：打开模式，默认打开模式为只读(r)
            - r
            - rb
            - r+
            - rb+
            - w
            - wb
            - w+
            - wb+
            - a
            - ab
            - a+
            - ab+
        buffering：指定读写文件的缓冲模式，默认为缓存模式（1）
            - 0：不缓存
            - 1：缓存
            - 大于1：表示缓冲区大小
"""
# 14.1.1 - 1 - 打开一个不存在的文件时先创建该文件
file = open('a.txt')
print(file)

# 14.1.1 - 2 - 以二进制形式打开文件
file = open('picture.jpg', 'rb')
print(file)

# 14.1.1 - 3 - 打开文件时指定编码方式
file = open('a.txt', 'r', encoding = 'utf-8')
print(file)

# 14.1.2 - 关闭文件
""" 
    语法格式：file.close()
    close方法先刷新缓冲区中还没有写入的信息，然后再关闭文件
"""
file.close()

# 14.1.3 - 打开文件时使用with语句
"""
    with语句格式：
        with expression as target:
            with-body
            - expression：用于指定一个表达式
            - target：用于指定一个变量，并且将expressioin的结果保存到该变量中
            - with-body：用于指定with语句体，可以是执行with语句后相关的一些操作语句。不执行可以使用pass语句代替。
"""
print("\n", "=" * 10, "Python经典应用", "=" * 10)
with open('a.txt', 'w') as file:
    pass
print("\n 即将显示...... \n")

# 14.1.4 - 写入文件内容
"""
    语法格式：file.write(string)
        - 前提：打开模式为w(可写)或者a(追加)
"""
with open('a.txt', 'w') as file:
    file.write("\nhello world")
    file.close()

# 14.1.5 - 读取文件
# 14.1.5 - 1 - 读取指定字符
"""
    语法格式：file.read([size])
        - size：可选，指定要读取的字符个数，省略则读取所有内容
        - 前提：打开文件可读，r(只读)或r+(读写)
        - 从文件开头读取
"""
with open('a.txt', 'r') as file:
    string = file.read(15)
    print(string)

"""
    移动文件指针到新的位置：seek()
    语法格式：file.seek(offset[, whence])
        - file：已经打开的文件对象
        - offset：指定移动的字符个数
        - whence：指定开始位置，默认为0。
            - 0：从文件开头
            - 1：从当前位置
            - 2：从文件尾
"""
with open('a.txt', 'r') as file:
    file.seek(5)
    string = file.read(8)
    print(string)

# 14.1.5 - 2 - 读取一行
"""
    一次读取大文件内容到内存，容易造成内存不足，通常采用逐行读取。
    语法格式：file.readline()
"""
print("\n", "=" * 20, "Python经典应用", "=" * 20, "\n")
with open('a.txt', 'r') as file:
    number = 0
    while True:
        number += 1
        line = file.readline()
        if line == '':
            break
        print(number, line, end = "\n")
print("\n", "=" * 20, "over", "=" * 20, "\n")

# 14.1.5 - 3 - 读取全部行
"""
    语法格式：file.readlines()
"""
print("\n", "=" * 20, "读取全部行", "=" * 20, "\n")
with open('a.txt', 'r') as file:
    message = file.readlines()
    print(message)
    print("\n", "=" * 25, "over", "=" * 25, "\n")

with open('a.txt', 'r') as file:
    message = file.readlines()
    for mes in message:
        print(mes)
    file.close()

''' 14.2 - 目录操作 '''
# 14.2.1 - os和os.path模块
"""
    os常用变量：
        - name：获取操作系统类型
                - nt：Windows系统
                - posix：Linux、Unix或Mac OS
        - linesep：获取当前系统换行符
        - sep：获取 当前系统所用路径分隔符
        - getcwd()：返回当前工作目录
        - listdir(path)：返回指定目录下文件和目录信息
        - mkdir(path[, mode])：创建目录
        - makedirs(path1/path2......[,mode])：创建多级目录
        - rmdir(path)：删除目录
        - removedir(path1/path2......)：删除多级目录
        - chdir(path)：把path设置为当前工作目录
        - walk(top[,topdown[,onerror]])：遍历目录树
    os.path常用操作目录函数：
        - abspath(path)：获取文件或目录的绝对路径
        - exists(path)：判断文件是否存在，存在返回True，否则返回False
        - join(path, name)：将目录与目录或文件名拼接起来
        - splitext()：分离文件名和扩展名
        - basename(path)：从一个目录中提取文件名
        - dirname(path)：从一个目录中提取文件路径，不包括文件名
        - isdir(path)：判断是否路径
"""
import os
print(os.name)
print(os.linesep)
print(os.sep)
print(os.getcwd())
print(os.listdir())
# os.mkdir('learn-14')
# os.rmdir('learn-14')
print(os.path.abspath('a.txt'))
print(os.path.exists('a.txt'))
print(os.path.join(os.getcwd(), 'a.txt'))
print(os.path.splitext('a.txt'))
print(os.path.basename(os.path.abspath('a.txt')))
print(os.path.dirname(os.path.abspath('a.txt')))
print(os.path.isdir(os.getcwd()))

# 14.2.2 - 路径
"""
    路径：用于定位一个文件或目录的字符串称为一个路径。
    - 相对路径
    - 绝对路径
    
    - 指定文件路径时需要对路径分割符“\”进行转义，即将“\”替换为“\\”；
    - 也可以用“/”代替
"""
# 14.2.2 - 1 - 相对路径
import os
print("\n相对路径：" + os.getcwd())
with open(r"a.txt") as file:
    pass
# 14.2.2 - 2 - 绝对路径
import os
print(os.path.abspath(r"test\hello.py"))
# 14.2.2 - 3 - 拼接路径：os.path.join(path1[,path2[, ......]])

# 14.2.3 - 判断目录是否存在：os.path.exists(path)

# 14.2.4 - 创建目录
# 14.2.4 - 1 - 创建一级目录
"""
    语法格式：os.mkdir(path, mode=0o777)
    - mode：默认0777，该参数在非UNIX系统上无效或被忽略
    - 目录已存在则报错，创建前可以先判断是否存在
"""
import os
# os.mkdir('learn-14')
path = 'learn-14'
if not os.path.exists(path):
    os.mkdir(path)
    print('创建目录成功!')
else:
    print('该目录已经存在！')

# 14.2.4 - 2 - 创建多级目录
"""
    语法格式：os.makedirs(name, mode = 0o777)
"""
path = "learn-14/demo"
if not os.path.exists(path):
    os.makedirs(path)
    print('创建多级目录成功！')
else:
    print('该目录已经存在！')

# 14.22.5 - 删除目录
"""
    语法格式：os.rmdir(path)
    - rmdir()只能删除空的目录
    - 删除非空目录：shutil.rmtree(path)
"""
import os
path = 'aa'
if os.path.exists(path):
    os.rmdir(path)
    print('目录删除成功！')
else:
    print('目录删除失败！')

# 14.2.6 - 遍历目录
"""
    语法格式：os.walk(top[, topdown][, onerror][, followlinks])
    - 只在Unix和Windows中有效
"""
import os
tuples = os.walk('test')
for temp in tuples:
    print(temp, "\n")

''' 14.3 - 高级文件操作 '''
"""
    os对文件高级操作：
        - access(path, accessmode)：获取对文件是否有指定的访问权限（读取/写入/执行权限）
        - chmod(path, mode)：修改path指定文件的访问权限
        - remove(path)：删除path指定文件目录
        - rename(src, dst)：将文件或目录src重命名为dst
        - stat(path)：返回path指定文件的信息
        - startfile(path[, operation])：使用关联应用程序打开path指定文件 
"""
# 14.3.1 - 删除文件
path = 'hello.txt'
with open(path, 'a') as file:
    pass

if os.path.exists(path):
    os.remove(path)
    print('文件删除成功！')
else:
    print('文件删除失败！')

# 14.3.2 - 重命名文件和目录
path = 'b.txt'
if os.path.exists(path):
    if not os.path.exists('c.txt'):
        os.rename(path, 'c.txt')
        print('重命名成功！')
    else:
        print('c.txt已经存在！')
else:
    print('文件不存在！')
    with open(path, 'a') as file:
        print('文件创建成功！')

# 14.3.3 - 获取文件基本信息
"""
    语法格式：obj = os.stat(path)
    obj对象属性：
        - st_mode：保护模式
        - st_dev：设备名
        - st_ino：索引号
        - st_uid：用户ID
        - st_nlink：硬链接号
        - st_gid：组ID
        - st_size：文件大小，单位为字节
        - st_atime：最后一次访问时间
        - st_mtime：最后一次修改时间
        - st_ctime：最后一次状态变化时间
"""
import time
path = 'a.txt'
if os.path.exists(path):
    fileinfo = os.stat(path)
    print(fileinfo)
    print(fileinfo.st_atime, int(fileinfo.st_atime))
    atime = fileinfo.st_atime
    atime_array = time.localtime(atime)
    adate = time.strftime("%Y-%m-%d %H:%M:%S", atime_array)
    print(atime, atime_array, adate)
    print(time.gmtime(), time.strftime("%Y", time.gmtime()))
