import pygame as pg
from pygame.locals import *
from load_resources import load_image


class Background_Graphics(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('./images/rift_bg.jpg', -1)
        window = pg.display.get_surface()
        self.area = window.get_rect()
        self.rect.topleft = 0, -175
        self.original_pos = self.rect.topleft
