import pygame as pg
from pygame.locals import *
from load_resources import load_colork_image
import random


class Obstacle(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_colork_image('./images/champs/gwen.png', -1)
        window = pg.display.get_surface()
        self.area = window.get_rect()
        self.rect.topleft = window.get_rect().right, 210
        self.original_pos = self.rect.left
        self.move = -8
        self.move_counter = 0
        self.move_delta = 10
        self.rand_gap = random.randint(100, 600)
        self.collided = False

    def chose_rand_file():
        randInt = random.randint(1, 4)

    def update(self):
        if self.collided:
            self.rand_gap = random.randint(100, 600)
            self.reset_object()
        elif self.move_counter:
            self.move_left()

    def move_left(self):
        self.move_counter += self.move_delta

        if self.is_offscreen():
            self.reset_object()
            self.rand_gap = random.randint(100, 600)

        self.rect = self.rect.move((self.move, 0))

    def is_offscreen(self):
        return self.rect.left < (0 - self.rect.width)
            
    def reset_object(self):
        self.rect.left = self.original_pos + self.rand_gap
        self.move_counter = 0

    def move_event(self):
        if not self.move_counter:
            self.move_counter = 1

    