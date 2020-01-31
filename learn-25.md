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
    class Enemy(pygame.sprite.Sprite):
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
  

### 25.4.2 - 游戏界面设置
- 初始化pygame，设置游戏界面大小、背景图片及标题等
    ```
    # 初始化pygame
    pygame.init()
    # 设置游戏界面大小、背景图片及标题
    # 游戏界面像素大小
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # 游戏界面标题
    pygame.display.set_caption('飞机大战')
    # 图标
    ic_launcher = pygame.image.load('resources/image/ic_launcher.png').convert_alpha()
    pygame.display.set_icon(ic_launcher)
    # 背景图
    background = pygame.image.load('resources/image/background.png').convert()
    # Game Over的背景图
    game_over = pygame.image.load('resources/image/gameover.png')
    # 飞机及子弹图片集合
    plane_img = pygame.image.load('resources/image/shoot.png')
    ```
- 创建主循环，初始化背景图，更新及退出等：
    ```
    # 判断游戏循环退出的参数
    running = True
    # 游戏主循环
    while running:
        # 绘制背景
        screen.fill(0)
        screen.blit(background, (0, 0))
        # 更新屏幕
        pygame.display.update()
        # 处理游戏退出
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    ```
### 25.4.3 - 用户交互操作等实现
- 在主循环中处理键盘输入等事件，增加游戏操作交互：
    ```
    # 获取键盘事件（上下左右按键）
    key_pressed = pygame.key.get_pressed()
    # 处理键盘事件（移动飞机等位置）
    if key_pressed[K_w] or key_pressed[K_UP]:
        player.moveUp()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        player.moveDown()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        player.moveLeft()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        player.moveRight()
    ```
  
### 25.4.4 - 对子弹对处理
- 在主循环中加入子弹处理，子弹由玩家飞机发出，并以一定速度向界面上方移动
    ```
    # 生成子弹，需要控制发射频率
    # 首先判断玩家飞机没有被击中
    if not player.is_hit:
        if shoot_frequency % 15 == 0:
            player.shoot(bullet_img)
        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0
    for bullet in player.bullets:
        # 以固定速度移动子弹
        bullet.move()
        # 移动出屏幕后删除子弹
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)
    # 显示子弹
    player.bullets.draw(screen)
    ```
  
### 25.4.5 - 敌机对处理
- 在主循环中加入敌机处理，敌机需要随机在界面上方产生，并以一定速度向下移动
    ```
    # 生成敌机，需要控制生成频率
    if enemy_frequency % 50 == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
        enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
        enemies1.add(enemy1)
    enemy_frequency += 1
    if enemy_frequency >= 100:
        enemy_frequency = 0
    for enemy in enemies1:
        # 移动敌机
        enemy.move()
        # 敌机与玩家飞机碰撞效果处理
        if pygame.sprite.collide_circle(enemy, player):
            enemies_down.add(enemy)
            enemies1.remove(enemy)
            player.is_hit = True
            break
        # 移动出屏幕后删除飞机
        if enemy.rect.top < 0:
            enemies1.remove(enemy)

    # 敌机被子弹击中效果处理
    # 将被击中对敌机对象添加到击毁敌机Group中，用来渲染击毁动画
    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
    for enemy_down in enemies1_down:
        enemies_down.add(enemy_down)

    # 绘制玩家飞机
    if not player.is_hit:
        screen.blit(player.image[player.img_index], player.rect)
        # 更换图片索引使飞机有动画效果
        player.img_index = shoot_frequency // 8
    else:
        # 玩家飞机被击中后对效果处理
        player.img_index = player_down_index // 8
        screen.blit(player.image[player.img_index], player.rect)
        player_down_index += 1
        if player_down_index > 47:
            # 击中效果处理完成后游戏结束
            running = False

    # 敌机被击中效果显示
    for enemy_down in enemies_down:
        if enemy_down.down_index == 0:
            pass
        if enemy_down.down_index > 7:
            enemies_down.remove(enemy_down)
            score += 100
            continue
        screen.blit(enemy_down.down_imgs[enemy_down.down_index // 2], enemy_down.rect)
        enemy_down.down_index += 1
    # 显示敌机
    enemies1.draw(screen)
    ```
### 25.4.6 - 显示游戏得分
- 在主循环中显示得分
    ```
  # 绘制当前得分
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect
  ```
  
### 25.4.7 - 游戏结束绘制游戏结束画面
- 游戏结束后要绘制对内容包含：游戏背景、最终分数、重新开始、排行榜等
    ```
    # 绘制游戏结束背景
    screen.blit(game_over, (0, 0))
    # 游戏Game Over后显示最终得分
    font = pygame.font.Font(None, 48)
    text = font.render('Score:' + str(score), True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 24
    screen.blit(text, text_rect)
    # 使用系统字体
    xtfont = pygame.font.SysFont('SimHei', 30)
    # 重新开始按钮
    textstart = xtfont.render('重新开始', True, (255, 0, 0))
    text_rect = textstart.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 120
    screen.blit(textstart, text_rect)
    # 排行榜按钮
    textstart = xtfont.render('排行榜', True, (255, 0, 0))
    text_rect = textstart.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 180
    screen.blit(textstart, text_rect)
    ```
  
### 25.4.8 - 更新排行榜内容
- 通过score.txt文件保存排行榜内容，在游戏结束时根据当前分数对score.txt文件中对排行榜内容进行更新
    ```
    import codecs
    """
    对文件对操作
    写入文本
    传入参数为content, strim, path
    """
    def write_txt(content, strim, path):
        f = codecs.open(path, strim, 'utf8')
        f.write(str(content))
        f.close()
    
    
    # 读取txt
    def read_txt(path):
        with open(path, 'r', encoding = 'utf8') as f:
            lines = f.readlines()
        return lines
  
    # 判断得分更新排行榜
    # 临时等变量在到排行榜到时候使用
    j = 0
    # 获取文件中内容转换成列表，使用mr分隔开内容
    arrayscore = read_txt(r'score.txt')
    if len(arrayscore) == 0:
        arrayscore = []
    else:
        arrayscore = arrayscore[0].split('mr')

    # 循环分数列表，在列表里排序
    for i in range(0, len(arrayscore)):
        if arrayscore[i] == '':
            arrayscore[i] = 0
        # 判断当前获得到分数是否大于排行榜上到分数
        if score > int(arrayscore[i]):
            # 大于排行榜上到内容，把分数和当前分数进行替换
            j = arrayscore[i]
            arrayscore[i] = str(score)
            score = 0
            continue
        # 替换下来的分数向下移动一位
        if int(j) > int(arrayscore[i]):
            k = arrayscore[i]
            arrayscore[i] = str(j)
            j = k

    if score > 0:
        arrayscore.append(str(score))

    # 循环分数列表，写入文档
    for i in range(0, len(arrayscore)):
        # 判断列表中第一个分数
        if i == 0:
            # 覆盖写入内容，追加mr方便分割内容
            write_txt(arrayscore[i] + 'mr', 'w', r'score.txt')
        else:
            # 判断是否为最后一个分数
            if (i == len(arrayscore) - 1):
                # 最近添加内容，最后一个分数不添加mr
                write_txt(arrayscore[i], 'a', r'score.txt')
            else:
                # 不是最后一个分数，添加的时候添加mr
                write_txt(arrayscore[i] + 'mr', 'a', r'score.txt')
    ```
  
### 25.4.9 - 判断鼠标到单击位置
- 添加游戏开始与排行榜文字按钮
    ```
    # 判断点击位置以及处理游戏退出
    while True:
        for event in pygame.event.get():
            # 关闭页面游戏退出
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # 鼠标单击
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 判断鼠标单击对位置是否为开始按钮位置范围内
                if screen.get_rect().centerx - 70 <= event.pos[0] \
                        and event.pos[0] <= screen.get_rect().centerx + 50 \
                        and screen.get_rect().centery + 100 <= event.pos[1] \
                        and screen.get_rect().centery + 140 >= event.pos[1]:
                    # 重新开始游戏
                    startGame()
                # 判断鼠标是否单击排行榜按钮
                if screen.get_rect().centerx - 70 <= event.pos[0] \
                        and event.pos[0] <= screen.get_rect().centerx + 50 \
                        and screen.get_rect().centery + 160 <= event.pos[1] \
                        and screen.get_rect().centery + 200 >= event.pos[1]:
                    # 显示排行榜
                    gameRanking()
    ```
  
### 25.4.10 - 游戏排行榜
    ```
    # 排行榜
    def gameRanking():
        screen2 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 绘制背景
        screen2.fill(0)
        screen2.blit(background, (0, 0))
        # 使用系统字体
        xtfont = pygame.font.SysFont('SimHei', 30)
        # 重新开始按钮
        textstart = xtfont.render('排行榜', True, (255, 0, 0))
        text_rect = textstart.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.centery = 50
        screen.blit(textstart, text_rect)
        # 使用系统字体
        xtfont = pygame.font.SysFont('SimHei', 30)
        # 重新开始按钮
        textstart = xtfont.render('重新开始', True, (255, 0, 0))
        text_rect = textstart.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.centery = screen.get_rect().centery + 120
        screen2.blit(textstart, text_rect)
        # 获取排行文档内容
        arrayscore = read_txt(r'score.txt')
        if len(arrayscore) > 0:
            arrayscore = arrayscore[0].split('mr')
        # 循环排行榜文件，显示排行
        for i in range(0, len(arrayscore)):
            # 游戏Game Over后显示最终得分
            font = pygame.font.Font(None, 48)
            # 排名从1到10
            k = i + 1
            text = font.render(str(k) + " " + arrayscore[i], True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = screen2.get_rect().centerx
            text_rect.centery = 80 + 30*k
            # 绘制分数内容
            screen2.blit(text, text_rect)
    ```