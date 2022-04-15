import pygame


class Ship:
    def __init__(self, ai_game):
        # 初始化飞船并设置其初始位置
        self.screen = ai_game.screen
        self.settings = ai_game.setttings

        # 加载飞船图像并获取其外接矩阵
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left:
            self.rect.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
