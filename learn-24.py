# code:     UTF-8
# author:   BeiYu
# datetime: 2020-01-09 21:03
# filename: learn-24.py
# tool:     PyCharm

# 24 - 谷歌小恐龙游戏

# 24.1 - 项目概述
"""
    谷歌浏览器在断网时会出现一只小恐龙，按下键盘空格键能激活该恐龙。
    通过空格键控制小恐龙的跳跃，躲避障碍物，根据躲避障碍物数计分。
"""

# 24.2 - 设计流程
# 24.3 - 系统预览
# 24.4 - 开发工具准备
"""
    操作系统：Window7
    开发工具：PyCharm
    开发模块：pygame
"""

# 24.5 - 谷歌小恐龙游戏的实现
# 24.5.1 - 主窗体的实现
"""
    (1) 创建文件目录
        - small_dinosuar
            - audio
            - image
            - dinosaur.py
            
    (2) 导入pygame库与pygame中常量库
        import pygame
        from pygame.locals import *         # 导入pygame中的常量
        
        SCREENWIDTH = 822                   # 窗体宽度
        SCREENHEIGHT = 260                  # 窗体高度
        FPS = 30                            # 更新画面时间
        
    (3) 创建mainGame()方法
        def mainGame():
            score = 0
            over = False
            global SCREEN, FPSCLOCK
            pygame.init()                                                   # 初始化
        
            FPSCLOCK = pygame.time.Clock()                                  # 创建Clock对象实例，控制每个循环多长时间运行一次
            SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))   # 创建窗体
            pygame.display.set_caption('小恐龙')                             # 设置窗体标题
        
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()                                              # 关闭窗体
                pygame.display.update()                                     # 更新整个窗体
                FPSCLOCK.tick(FPS)                                          # 循环应该多长时间运行一次
        
        
        if __name__ == '__main__':
            mainGame()
"""

# 24.5.2 - 滚动地图的显示
"""
    渲染两个地图背景图片，往左无限循环滚动。
    (1) 创建MyMap滚动地图类
        # 定义一个滚动地图类
        class MyMap():
            def __init__(self, x, y):
                self.bg = pygame.image.load("image/bg.png").convert_alpha()     # 加载背景图片
                self.x = x
                self.y = y
                
    (2) 在MyMap类中创建map_rolling()方法，根据地图背景图片x坐标判断是否移出窗体
            def map_rolling(self):                                              
                if self.x < -790:                                               # 小于-790说明地图已经移动完毕
                    self.x = 800                                                # 给地图一个新坐标
                else:
                    self.x -= 5                                                 # 5个像素向左移动
                    
    (3) 在MyMap类中创建map_update()方法，实现地图无限滚动效果 
            def map_update(self):
                SCREEN.blit(self.bg, (self.x, self.y))
                
    (4) 在mainGame()方法中，创建两个背景图片对象
        bg1 = MyMap(0, 0)                                               # 创建地图对象
        bg2 = MyMap(800, 0)
        
    (5) 在mainGame()方法循环中，实现无限循环滚动的地图
        if not over:
            bg1.map_update()                                        # 绘制地图起到更新地图的作用
            bg1.map_rolling()                                       # 地图移动
            bg2.map_update()
            bg2.map_rolling()
"""

# 24.5.3 - 可以跳跃的小恐龙
"""
    逻辑：
        - 制定小恐龙的固定座标
        - 判断是否按下空格键
            - 按下：开启小恐龙跳跃开关，并让小恐龙以5个像素距离向上移动
            - 到达顶部边缘：小恐龙以5个像素距离向下移动，回到地面后关闭跳跃开关
"""