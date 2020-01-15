# 25 - 飞机大战游戏

## 25.1 - 概述
- 玩家移动自己的飞机，躲避迎面而来的其他飞机
- 玩家飞机发射炮弹，打掉其他飞机，赢取分数
- 玩家飞机撞上其他飞机，游戏结束

## 25.2  - 系统预览
- 游戏运行页面
- 游戏结束页面
- 排行榜页面

## 25.3 - 开发工具
- 操作系统：Windows10
- 开发工具：PyCharm
- 开发模块：pygame

## 25.4 - 飞机大战游戏的实现
### 25.4.1 - 主窗体的实现
步骤：
- 1.创建文件
    - foo：项目文件夹
    - —— image：图片资源
    - —— score.txt：保存分数
    - —— main.py：代码
- 2、导入pygame，并定义窗体
    ```
    import pygame
    from pygame.locals import *
    from sys import exit
    import random
    
    # 设置游戏屏幕大小
    SCREEN_WIDTH = 480
    SCREEN_HEIGHT = 800
    ```
- 3、游戏角色分析创建
    - 玩家飞机：Player
        - 射击
        - 移动【上、下、左、右】
    - 敌机：Enemy
        - 移动
    - 子弹：Bullet
        - 移动

    ```# 子弹类
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, bullet_img, init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet_img
            self.rect = self.image.get_rect()
            self.rect.midbottom = init_pos
            self.speed = 10
    
        def move(self):
            self.rect.top -= self.speed
    
    
    # 玩家飞机类
    class Player(pygame.sprite.Sprite):
        def __init__(self, plane_img, player_rect, init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = []                         # 用来存储玩家飞机图片的列表
            for i in range(len(player_rect)):
                self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
            self.rect = player_rect[0]              # 初始化图片所在的矩形
            self.rect.topleft = init_pos            # 初始化矩形的左上角坐标
            self.speed = 8                          # 初始化玩家飞机速度
            self.bullets = pygame.sprite.Group()    # 玩家飞机所发射的子弹的合集
            self.img_index = 0                      # 玩家飞机图片索引
            self.is_hit = False                     # 玩家是否被击中
    
        # 发射子弹
        def shoot(self, bullet_img):
            bullet = Bullet(bullet_img, self.rect.midtop)
            self.bullets.add(bullet)
    
        # 向上移动，需要判断边界
        def moveUp(self):
            if self.rect.top <= 0:
                self.rect.top = 0
            else:
                self.rect.top -= self.speed
    
        # 向下移动，需要判断边界
        def moveDown(self):
            if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
                self.rect.top = SCREEN_HEIGHT - self.rect.height
            else:
                self.rect.top += self.speed
    
        # 向左移动，需要判断边界
        def moveLeft(self):
            if self.rect.left <= 0:
                self.rect.left = 0
            else:
                self.rect.left -= self.speed
    
        # 向右移动，需要判断边界
        def moveRight(self):
            if self.rect.left >= SCREEN_WIDTH - self.rect.width:
                self.rect.left = SCREEN_WIDTH - self.rect.width
            else:
                self.rect.left += self.speed
    
    
    # 敌机类
    class Enemy(pygame.sprite.Sprite)r:
        def __init__(self, enemy_img, enemy_down_imgs, init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = enemy_img
            self.rect = self.image.get_rect()
            self.rect.topleft = init_pos
            self.down_imgs = enemy_down_imgs
            self.speed = 2
            self.down_index = 0
    
        # 敌机移动，边界判断及删除在游戏主循环里处理
        def move(self):
            self.rect.top += self.speed```

