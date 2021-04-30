import pygame as pg
from pygame.locals import *
from load_resources import load_colork_image


class Obstacle(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_colork_image('./images/obstacle_box.png', -1)
        window = pg.display.get_surface()
        self.area = window.get_rect()
        self.rect.topleft = 0, 0
        self.original_pos = self.rect.topleft

    