# code:     UTF-8
# author:   BeiYu
# datetime: 2020-01-09 21:35
# filename: dinosaur.py
# tool:     PyCharm
import pygame
from pygame.locals import *         # 导入pygame中的常量
from itertools import cycle         # 导入迭代工具

SCREENWIDTH = 822                   # 窗体宽度
SCREENHEIGHT = 260                  # 窗体高度
FPS = 30                            # 更新画面时间


# 定义一个滚动地图类
class MyMap():
    def __init__(self, x, y):
        self.bg = pygame.image.load("image/bg.png").convert_alpha()     # 加载背景图片
        self.x = x
        self.y = y

    def map_rolling(self):                                              # 根据地图背景图片x坐标判断是否移出窗体
        if self.x < -790:                                               # 小于-790说明地图已经移动完毕
            self.x = 800                                                # 给地图一个新坐标
        else:
            self.x -= 5                                                 # 5个像素向左移动

    def map_update(self):
        SCREEN.blit(self.bg, (self.x, self.y))


# 恐龙类
class Dinosaur():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)                                 # 初始化小恐龙矩形
        self.jumpState = False                                              # 跳跃的状态
        self.jumpHeight = 130                                               # 跳跃的高度
        self.lowest_y = 120                                                 # 最低坐标
        self.jumpValue = 0                                                  # 跳跃增变量

        self.dinosaurIndex = 0                                              # 小恐龙动图索引
        self.dinosaurIndexGen = cycle([0, 1, 2])

        self.dinosaur_img = (                                               # 加载小恐龙图片
            pygame.image.load("image/dinosaur1.png").convert_alpha(),
            pygame.image.load("image/dinosaur2.png").convert_alpha(),
            pygame.image.load("image/dinosaur3.png").convert_alpha()
        )

        self.jump_audio = pygame.mixer.Sound('audio/jump.wav')              # 跳
        self.rect.size = self.dinosaur_img[0].get_size()
        self.x = 50                                                         # 绘制恐龙x坐标
        self.y = self.lowest_y                                              # 绘制恐龙y坐标
        self.rect.topleft =  (self.x, self.y)


def mainGame():
    score = 0
    over = False
    global SCREEN, FPSCLOCK
    pygame.init()                                                   # 初始化

    FPSCLOCK = pygame.time.Clock()                                  # 创建Clock对象实例，控制每个循环多长时间运行一次
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))   # 创建窗体
    pygame.display.set_caption('小恐龙')                             # 设置窗体标题

    bg1 = MyMap(0, 0)                                               # 创建地图对象
    bg2 = MyMap(800, 0)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()                                              # 关闭窗体
        pygame.display.update()                                     # 更新整个窗体
        FPSCLOCK.tick(FPS)                                          # 循环应该多长时间运行一次

        if not over:
            bg1.map_update()                                        # 绘制地图起到更新地图的作用
            bg1.map_rolling()                                       # 地图移动
            bg2.map_update()
            bg2.map_rolling()


if __name__ == '__main__':
    mainGame()


