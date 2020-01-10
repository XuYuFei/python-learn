# code:     UTF-8
# author:   BeiYu
# datetime: 2020-01-09 21:35
# filename: dinosaur.py
# tool:     PyCharm
import pygame
from pygame.locals import *         # 导入pygame中的常量
from itertools import cycle         # 导入迭代工具
import random                       # 随机数

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
        self.lowest_y = 140                                                 # 最低坐标
        self.jumpValue = 0                                                  # 跳跃增变量

        self.dinosaurIndex = 0                                              # 小恐龙动图索引
        self.dinosaurIndexGen = cycle([0, 1, 2])

        self.dinosaur_img = (                                               # 加载小恐龙图片
            pygame.image.load("image/dinosaur1.png").convert_alpha(),
            pygame.image.load("image/dinosaur2.png").convert_alpha(),
            pygame.image.load("image/dinosaur3.png").convert_alpha()
        )

        self.jump_audio = pygame.mixer.Sound('audio/jump.wav')              # 加载音效
        self.rect.size = self.dinosaur_img[0].get_size()                    # 设置小恐龙矩形大小
        self.x = 50                                                         # 绘制恐龙x坐标
        self.y = self.lowest_y                                              # 绘制恐龙y坐标
        self.rect.topleft = (self.x, self.y)                                # 设置左上角为准

    # 跳状态
    def jump(self):
        self.jumpState = True

    # 小恐龙移动
    def move(self):
        if self.jumpState:                                                  # 当起跳的时候
            if self.rect.y >= self.lowest_y:                                # 如果站在地上
                self.jumpValue = -5                                         # 以5个像素值向上移动
            if self.rect.y <= self.lowest_y - self.jumpHeight:              # 恐龙到达顶部回落
                self.jumpValue = 5                                          # 以5个像素值向下移动
            self.rect.y += self.jumpValue                                   # 通过循环改变恐龙的y坐标
            if self.rect.y >= self.lowest_y:                                # 如果恐龙回到地面
                self.jumpState = False                                      # 关闭跳跃状态

    # 绘制恐龙
    def draw_dinosaur(self):
        dinosaurIndex = next(self.dinosaurIndexGen)                             # 匹配恐龙动图
        SCREEN.blit(self.dinosaur_img[dinosaurIndex], (self.x, self.rect.y))    # 绘制小恐龙


# 障碍物类
class Obstacle():
    score = 1   # 分数

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)                                 # 初始化障碍物矩形

        self.stone = pygame.image.load("image/stone.png").convert_alpha()   # 加载障碍物图片
        self.cacti = pygame.image.load("image/cacti.png").convert_alpha()

        self.numbers = (                                                    # 加载分数图片
            pygame.image.load('image/0.png').convert_alpha(),
            pygame.image.load('image/1.png').convert_alpha(),
            pygame.image.load('image/2.png').convert_alpha(),
            pygame.image.load('image/3.png').convert_alpha(),
            pygame.image.load('image/4.png').convert_alpha(),
            pygame.image.load('image/5.png').convert_alpha(),
            pygame.image.load('image/6.png').convert_alpha(),
            pygame.image.load('image/7.png').convert_alpha(),
            pygame.image.load('image/8.png').convert_alpha(),
            pygame.image.load('image/9.png').convert_alpha()
        )
        self.score_audio = pygame.mixer.Sound('audio/score.wav')            # 加载加分音效

        r = random.randint(0, 1)                                            # 0和1随机数
        if r == 0:
            self.image = self.stone                                         # 0为石头
        else:
            self.image = self.cacti                                         # 1为仙人掌

        self.rect.size = self.image.get_size()                              # 根据障碍物位图的宽高来设置矩形
        self.width, self.height = self.rect.size                            # 获取位图宽高

        self.x = 800                                                        # 障碍物绘制坐标
        self.y = 200 - (self.height / 2)
        self.rect.center = (self.x, self.y)

    # 障碍物移动
    def obstacle_move(self):
        self.rect.x -= 5

    # 绘制障碍物
    def draw_obstacle(self):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    # 获取分数
    def getScore(self):
        self.score
        tmp = self.score
        if tmp == 1:
            self.score_audio.play()                                 # 播放加分音乐
        self.score = 0
        return tmp

    # 显示分数
    def showScore(self, score):
        """ 在窗体顶部中间位置显示分数 """
        self.scoreDigits = [int(x) for x in list(str(score))]
        totalWidth = 0                                                          # 要显示所有数字的总宽度
        for digit in self.scoreDigits:
            totalWidth += self.numbers[digit].get_width()                       # 获取计分图片宽度
        Xoffset = (SCREENWIDTH - totalWidth) / 2                                # 分数横向位置
        for digit in self.scoreDigits:
            SCREEN.blit(self.numbers[digit], (Xoffset, SCREENHEIGHT * 0.1))     # 绘制分数
            Xoffset += self.numbers[digit].get_width()                          # 随着数字增加改变位置


# 游戏结束方法
def game_over():
    bump_audio = pygame.mixer.Sound('audio/bump.wav')                       # 撞击
    bump_audio.play()                                                       # 播放撞击音效

    screen_w = pygame.display.Info().current_w                              # 获取窗体宽度、高度
    screen_h = pygame.display.Info().current_h

    over_img = pygame.image.load('image/gameover.png').convert_alpha()      # 加载游戏结束的图片
    SCREEN.blit(over_img, ((screen_w - over_img.get_width()) / 2, (screen_h - over_img.get_height()) / 2))


def mainGame():
    score = 0
    over = False
    global SCREEN, FPSCLOCK
    pygame.init()                                                   # 初始化

    FPSCLOCK = pygame.time.Clock()                                  # 创建Clock对象实例，控制每个循环多长时间运行一次
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))   # 创建窗体
    pygame.display.set_caption('小恐龙')                             # 设置窗体标题

    # 创建地图对象
    bg1 = MyMap(0, 0)
    bg2 = MyMap(800, 0)

    # 创建恐龙对象
    dinosaur = Dinosaur()

    addObstacleTimer = 0                                            # 添加障碍物的时间
    list = []                                                       # 障碍物对象列表

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()                                              # 关闭窗体
            if event.type == KEYDOWN and event.key == K_SPACE:
                if dinosaur.rect.y >= dinosaur.lowest_y:            # 如果恐龙在地面上
                    dinosaur.jump()                                 # 开启恐龙跳的状态
                    dinosaur.jump_audio.play()                      # 播放小恐龙跳跃音效

                if over:                                            # 判断游戏结束的开关是否开启
                    mainGame()                                      # 如果开启调用mainGame()方法重启游戏

        addObstacleTimer += 20                                      # 增加障碍物时间
        pygame.display.update()                                     # 更新整个窗体
        FPSCLOCK.tick(FPS)                                          # 循环应该多长时间运行一次

        if not over:
            bg1.map_update()                                        # 绘制地图起到更新地图的作用
            bg1.map_rolling()                                       # 地图移动
            bg2.map_update()
            bg2.map_rolling()

            dinosaur.move()                                         # 恐龙移动
            dinosaur.draw_dinosaur()                                # 绘制恐龙

            # 计算障碍物间隔时间
            if addObstacleTimer >= 1300:
                r = random.randint(0, 100)
                if r > 40:
                    obstacle = Obstacle()                           # 创建障碍物对象
                    list.append(obstacle)                           # 将障碍物对象添加到列表中
                addObstacleTimer = 0                                # 重置添加障碍物时间

            # 循环遍历障碍物
            for i in range(len(list)):
                list[i].obstacle_move()                             # 障碍物移动
                list[i].draw_obstacle()                             # 绘制障碍物

                # 判断恐龙与障碍物是否碰撞
                if pygame.sprite.collide_rect(dinosaur, list[i]):
                    over = True                                     # 碰撞后开启结束开关
                    game_over()                                     # 调用游戏结束的方法
                else:
                    # 判断小恐龙是否跃过了障碍物
                    if (list[i].rect.x + list[i].rect.width) < dinosaur.rect.x:
                        score += list[i].getScore()                 # 加分
                list[i].showScore(score)                            # 显示分数


if __name__ == '__main__':
    mainGame()


