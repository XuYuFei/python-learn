# *_* code: UTF-8 *_*
# author:   Beiyu
# datetime: 2019-12-28 11:35
# filename: learn-20.PY
# tool:     PyCharm
""" 20 - pygame游戏框架 """

# 20.1 - 初识pygame
"""
    pygame是跨平台Python模块，专为电子游戏设计，包含图像、声音。
    创建在SDL(Simple Direct Media Layer)基础上，允许实时电子游戏研发而无需被低级语言束缚。
"""

# 20.1.1 - 安装pygame
"""
    命令：pip install pygame
    检查安装：
        import pygame
        pygame.ver
"""
import pygame
pygame.ver

# 20.1.2 - pygame常用模块
"""
    常用模块：
    - pygame.cdrom：访问光驱
    - pygame.cursors：加载光标
    - pygame.display：访问显示设备
    - pygame.draw：绘制形状、线和点
    - pygame.event：管理事件
    - pygame.font：使用字体
    - pygame.image：加载和存储图片
    - pygame.joystick：使用游戏手柄或者类似的设备
    - pygame.key：读取键盘按键
    - pygame.mixer：声音
    - pygame.mouse：鼠标
    - pygame.movie：播放视频
    - pygame.music：播放音频
    - pygame.overlay：访问高级视频叠加
    - pygame.rect：管理矩形区域
    - pygame.sndarray：操作声音数据
    - pygame.sprite：操作移动图像
    - pygame.surface：管理图像和屏幕
    - pygame.surfarray：管理点阵图像数据
    - pygame.time：管理时间和帧信息
    - pygame.transform：缩放和移动图像
"""
"""
import sys
import pygame

pygame.init()                           # 初始化pygame
size = width, height = 320, 240         # 设置窗口
screen = pygame.display.set_mode(size)  # 显示窗口

# 执行死循环，确保窗口一直显示
while True:
    for event in pygame.event.get():    # 遍历所有事件
        if event.type == pygame.QUIT:   # 如果点击关闭窗口，则退出
            sys.exit()

pygame.quit()                           # 退出pygame
"""

# 20.2 - pygame的基本使用

"""
    display模块的常用方法：
        - pygame.display.init：初始化display模块
        - pygame.display.quit：结束display模块
        - pygame.display.get_init：如果display模块已经被初始化，则返回True
        - pygame.display.set_mode：初始化一个准备显示的界面
        - pygame.display.get_surface：获取当前surface对象
        - pygame.display.flip：更新整个待显示的surface对象到屏幕上
        - pygame.display.update：更新部分内容显示到屏幕上，如果没有参数则与flip功能相同
        
    Surface对象常用方法：
        - pygame.Surface.blit：将一个图像画到另一个图像上
        - pygame.Surface.convert：转换图像的像素格式
        - pygame.Surface.convert_alpha：转化图像的像素格式，包含alpha通道的转换
        - pygame.Surface.fill：使用颜色填充Surface
        - pygame.Surface.get_rect：获取Surface的矩形区域
"""
import sys
import pygame

pygame.init()                                   # 初始化pygame
size = width, height = 640, 480                 # 设置窗口
screen = pygame.display.set_mode(size)          # 显示窗口
color = (0, 0, 0)                               # 设置颜色

ball = pygame.image.load('./images/ball.png')   # 加载图片
ballrect = ball.get_rect()                      # 获取矩形区域

speed = [5, 5]                                  # 设置移动的x轴，y轴距离
clock = pygame.time.Clock()                     # 设置时钟
while True:
    clock.tick(60)                              # 每秒执行60次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)             # 移动小球

    # 碰到左右边缘
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color)                          # 填充颜色
    screen.blit(ball, ballrect)                 # 将图片画到窗口上
    pygame.display.flip()                       # 更新全部显示

pygame.quit()















