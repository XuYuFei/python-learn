# *_* code: UTF-8 *_*
# author:   Beiyu
# datetime: 2019-12-27 11:39
# filename: learn-19.PY
# tool:     PyCharm
""" 19 - 常用的GUI框架 """
''' 19.1 - 初识GUI '''
# 19.1.1 - 什么是GUI
# GUI：Graphical User Interface(图形用户界面)

# 19.1.2 - 常用的GUI框架
# wxPython、Kivy、Flexx、PyQt、Tkinter、Pywin32、PyGTK、pyui4win

''' 19.2 - wxPython框架的使用 '''
# 19.2.1 - 安装wxPython
# 命令：pip install -U wxPython

# 19.2.2 - 创建一个wx.App的子类
"""
    创建和使用一个wx.App子类需要执行如下4个步骤：
    1.定义这个子类；
    2.在定义的子类中写一个OnInit()初始化方法；
    3.在程序主要部分创建这个类的一个实例；
    4.调用应用程序实例的MainLoop()方法，这个方法将程序的控制权交给wxPython;
"""
"""
import wx


class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Hello Python')
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
"""

# 19.2.3 - 直接使用wx.App
"""
import wx
app = wx.App()
frame = wx.Frame(None, title = 'Hello wxPython')
frame.Show()
app.MainLoop()
"""

# 19.2.4 - 使用wx.Frame框架
"""
    wx.Frame是所有框架的父类。
    当创建wx.Frame的子类时，子类应该调用其父类的构造器wx.Frame.__init__()。
    语法格式：
        - wx.Frame(parent, id = -1, title = '', pos = wx.DefaultPosition, size = wx.DefaultSize, 
            style = wx.DEFAULT_FRAME_STYLE, name = 'frame')
        -- parent：框架父窗口。如果是顶级窗口，这个值是None;
        -- id：关于新窗口的wxPython ID号。通常设为-1，让wxPython自动生成一个新的ID;
        -- title：窗口标题；
        -- pos：一个wx.Point对象，默认(-1, -1);
        -- size：一个wx.Size对象，默认(-1, -1);
        -- style：指定窗口类型的常量。可以使用或运算来组合它们；
        -- name：框架内在的名字。可以使用它来寻找这个窗口。
"""
"""
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='创建Frame', pos=(100, 100), size=(300, 300))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
"""

# 19.2.5 - 常用控件

# 19.2.5 - 1 - StaticText文本类
"""
    wx.StaticText类的构造函数语法格式：
        - wx.StaticText(parent, id, label, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, name = 'staticText')
            - parent：父窗口部件；
            - id：标识符。使用-1可以自动创建一个唯一的标识；
            - label：显示在静态控件中的文本内容；
            - pos：一个wx.Point或一个Python元组；
            - size：一个wx.Size或一个Python元素；
            - style：样式标记；
            - name：对象的名字；    
    wx.Font类设置字体，构造函数：
        - wx.Font(pointSize, family, style, weight, underline = false, faceName = '', encoding = wx.FONTENCODING_DEFAULT)
"""
"""
import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = '创建StaticText类', pos = (200, 200), size = (600, 400))
        panel = wx.Panel(self) # 创建面板

        # 创建标题，并设置字体
        title = wx.StaticText(panel, label = 'Python之禅——Tim Peters', pos = (100, 20))
        font = wx.Font(16, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        title.SetFont(font)

        # 创建文本
        wx.StaticText(panel, label = '优美胜于丑陋', pos = (50, 50))
        wx.StaticText(panel, label = '明了胜于晦涩', pos = (50, 70))
        wx.StaticText(panel, label = '简介胜于复杂', pos = (50, 90))
        wx.StaticText(panel, label = '复杂胜于凌乱', pos = (50, 110))
        wx.StaticText(panel, label = '扁平胜于嵌套', pos = (50, 130))
        wx.StaticText(panel, label = '间隔胜于紧凑', pos = (50, 150))
        wx.StaticText(panel, label = '可读性很重要', pos = (50, 170))
        wx.StaticText(panel, label = '即便假借特例的实用性之名，也不可违背这些规则', pos = (50, 190))
        wx.StaticText(panel, label = '不要包容所有错误，除非你确定需要这样做', pos = (50, 210))
        wx.StaticText(panel, label = '当存在多种可能，不要尝试去猜测', pos = (50, 230))
        wx.StaticText(panel, label = '而是尽量找一种，最好是唯一一种明显的解决方案', pos = (50, 250))
        wx.StaticText(panel, label = '虽然这并不容易，因为你不是Python之父', pos = (50, 270))
        wx.StaticText(panel, label = '做也许好过不做，但不假思索就动手还不如不做', pos = (50, 290))
        wx.StaticText(panel, label = '如果你无法向人描述你的方案，那肯定不是一个好方案，反之亦然', pos = (50, 310))
        wx.StaticText(panel, label = '命名空间是一种绝妙的理念，我们应当多加利用', pos = (50, 330))

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
"""

# 19.2.5 - 2 - TextCtrl输入文本类
"""
    wx.TextCtrl类构造函数语法格式：
        - wx.TextCtrl(parent, id, value = '', pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, validator = wx.DefaultValidator, name = TextCtrlNameStr)
            - parnet, id, pos, size, style, name：同wx.StaticText
            - style：单行wx.TextCtrl样式
                - wx.TE_CENTER：文本居中；
                - wx.TE_LEFT：左对齐，默认；
                - wx.TE_NOHIDESEL：文本始终高亮显示，只适用于Windows；
                - wx.TE_PASSWORD：密码；
                - wx.TE_PROCESS_ENTER：响应<Enter>键；
                - wx.TE_PROCESS_TAB：响应<TAB>键；
                - wx.TE_READONLY：只读；
                - wx.TE_RIGHT：右对齐；
            - value：初始文本；
            - validator：过滤数据；
"""

# 19.2.5 - 3 - Button按钮类
"""
    wx.Button类的构造函数：
        - wx.Button(parent, id, label, pos, size = wx.DefaultSize, style = 0, validator, name = 'button')
"""
"""
import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = '创建TextCtrl类', size = (400, 300))
        # 创建面板
        panel = wx.Panel(self)
        # 创建文本和输入框
        self.title = wx.StaticText(panel, label = '请输入用户名和密码', pos = (140, 20))
        self.label_user = wx.StaticText(panel, label = '用户名', pos = (50, 50))
        self.text_user = wx.TextCtrl(panel, pos = (100, 50), size = (235, 25), style = wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label = '密  码', pos = (50, 90))
        self.text_pwd = wx.TextCtrl(panel, pos = (100, 90), size = (235, 25), style = wx.TE_PASSWORD)
        # 创建“确定”和“取消”按钮
        self.bt_confirm = wx.Button(panel, label = '确定', pos = (105, 130))
        self.bt_cancel = wx.Button(panel, label = '取消', pos = (195, 130))

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
"""

# 19.2.6 - BoxSize布局
"""
    sizer是用于自动布局一组窗口控件的算法。sizer被附加到一个容器中，通常是一个框架或面板。
    在父容器中创建的子窗口空间必须被分别添加到sizer中。当sizer被附加到容器时，它随后就可以管理它所包含的子布局。
    wxPython提供了5个sizer:
        - BoxSizer
        - GridSizer
        - FlexGridSizer
        - GridBagSizer
        - StaticBoxSizer
"""

# 19.2.6 - 1 - 什么是BoxSizer
"""
    BoxSizer是wxPython提供的sizer中的最简单和最灵活的。
    一个BoxSizer是一个垂直列或水平行，窗口部件从左至右或从上到下布置在一条线上。
"""

# 19.2.6 - 2 - 使用BoxSizer布局
"""
    尺寸器会管理组件的尺寸。
    只要将部件添加到尺寸器上，再加上一些布局参数，然后让尺寸器自己去管理父组件的尺寸。
    Add()方法语法格式：
        - Box.add(control, proportion, flag, border)
            - control：要添加的控件；
            - proportion：空间比例；
            - flag：flag参数与bordr参数结合使用可以指定边距宽度，包括以下选项：
                - wx.LEFT：左边距
                - wx.RIGHT：右边距
                - wx.BOTTOM：底边距
                - wx.TOP：上边距
                - wx.ALL：上下左右4边距
                - wx.ALIGN_LEFT：左边对齐
                - wx.ALIGN_RIGHT：右边对齐
                - wx.ALIGN_TOP：顶部对齐
                - wx.ALIGN_BOTTOM：底部对齐
                - wx.ALIGN_CENTER_VERTICAL：垂直对齐
                - wx.ALIGN_CENTER_HORIZONTAL：水平对齐
                - wx.ALIGN_CENTER：居中对齐
                - wx.EXPAND：所添加控件将占有sizer定位方向上所有可用控件
            - border：控制所添加控件的边距，就是在部件之间添加一些像素的空白
"""
"""
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '用户登录', size=(400, 300))
        # 创建面板
        panel = wx.Panel(self)

        # 创建“确定”和“取消”按钮，并绑定事件
        self.bt_confirm = wx.Button(panel, label = '确定')
        self.bt_cancel = wx.Button(panel, label = '取消')

        # 创建文本，左对齐
        self.title = wx.StaticText(panel, label='请输入用户名和密码')
        self.label_user = wx.StaticText(panel, label = '用户名：')
        self.text_user = wx.TextCtrl(panel, style = wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label = '密   码：')
        self.text_pwd = wx.TextCtrl(panel, style = wx.TE_PASSWORD)

        # 添加容器，容器中的控件横向排列
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion = 0, flag = wx.ALL, border = 5)
        hsizer_user.Add(self.text_user, proportion = 1, flag = wx.ALL, border = 5)

        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd, proportion = 0, flag = wx.ALL, border = 5)
        hsizer_pwd.Add(self.text_pwd, proportion = 1, flag = wx.ALL, border = 5)

        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion = 0, flag = wx.ALIGN_CENTER, border = 5)
        hsizer_button.Add(self.bt_cancel, proportion = 1, flag = wx.ALIGN_CENTER, border = 5)

        # 添加容器，容器中的控件按横向排列
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER, border=15)
        vsizer.Add(hsizer_user, proportion = 0, flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 45)
        vsizer.Add(hsizer_pwd, proportion = 0, flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 45)
        vsizer.Add(hsizer_button, proportion = 0, flag = wx.ALIGN_CENTER | wx.TOP, border = 15)
        panel.SetSizer(vsizer)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
"""
# 19.2.7 - 事件处理

# 19.2.7 - 1 - 什么是事件
# 用户执行的动作就叫作事件。

# 19.2.7 - 2 - 绑定事件
"""
    控件Bind()方法将事件处理函数绑定到给定的事件上；
    例：
    button.Bind(wx.EVT_BUTTON, OnclickSubmit)
        - wx.EVT_BUTTON：事件类型为按钮类型
        - OnclickSubmit：方法名，事件发生时执行该方法
"""

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '用户登录', size=(400, 300))
        # 创建面板
        panel = wx.Panel(self)

        # 创建“确定”和“取消”按钮，并绑定事件
        self.bt_confirm = wx.Button(panel, label = '确定')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label = '取消')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)

        # 创建文本，左对齐
        self.title = wx.StaticText(panel, label='请输入用户名和密码')
        self.label_user = wx.StaticText(panel, label = '用户名：')
        self.text_user = wx.TextCtrl(panel, style = wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label = '密   码：')
        self.text_pwd = wx.TextCtrl(panel, style = wx.TE_PASSWORD)

        # 添加容器，容器中的控件横向排列
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion = 0, flag = wx.ALL, border = 5)
        hsizer_user.Add(self.text_user, proportion = 1, flag = wx.ALL, border = 5)

        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd, proportion = 0, flag = wx.ALL, border = 5)
        hsizer_pwd.Add(self.text_pwd, proportion = 1, flag = wx.ALL, border = 5)

        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion = 0, flag = wx.ALIGN_CENTER, border = 5)
        hsizer_button.Add(self.bt_cancel, proportion = 1, flag = wx.ALIGN_CENTER, border = 5)

        # 添加容器，容器中的控件按横向排列
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER, border=15)
        vsizer.Add(hsizer_user, proportion = 0, flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 45)
        vsizer.Add(hsizer_pwd, proportion = 0, flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 45)
        vsizer.Add(hsizer_button, proportion = 0, flag = wx.ALIGN_CENTER | wx.TOP, border = 15)
        panel.SetSizer(vsizer)

    def OnclickSubmit(self, event):
        """ 单击“确定”按钮执行方法 """
        message = ''
        username = self.text_user.GetValue()    # 获取输入的用户名
        password = self.text_pwd.GetValue()     # 获取输入的密码
        if username == '' or password == '':
            message = '用户名或密码不能为空'
        elif username == 'hello' and password == 'world':
            message = '登录成功'
        else:
            message = '用户名和密码不匹配'
        wx.MessageBox(message)

    def OnclickCancel(self, event):
        """ 单击“取消”按钮，执行方法 """
        self.text_user.SetValue('')
        self.text_pwd.SetValue('')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()