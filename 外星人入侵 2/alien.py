import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # 表示单个外星人
    def __init__(self, ai_game):
        # 初始化外星人并设置起始位置
        super().__init__()
        self.screen = ai_game.screen
        # 加载图形并设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # 外星人出现在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的精准水平位置
        self.x = float(self.rect.x)
