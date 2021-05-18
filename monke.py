import pygame as pg
from pygame.locals import *
from load_resources import load_color_image


class Monke(pg.sprite.Sprite):
    """Monke go jump"""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_color_image('./images/monke_ride_gp_vlad.png', -1)
        window = pg.display.get_surface()
        self.area = window.get_rect()
        self.rect.topleft = 10, 150
        self.move = -5
        self.jump_counter = 0
        self.jump_delta = 10
        self.original_pos = self.rect.topleft
        self.lives = 10

    def update(self):
        if self.jump_counter:
            self.go_up()

    def go_up(self):
        self.jump_counter += self.jump_delta

        if self.jump_counter >= 300:
            self.invert_vectors()
        elif self.jump_counter < 0:
            self.jump_counter = 0
            self.rect.topleft = self.original_pos
            self.invert_vectors()

        self.rect = self.rect.move((0, self.move))

    def invert_vectors(self):
        self.jump_delta = -self.jump_delta
        self.move = -self.move

    def jump_event(self):
        if not self.jump_counter:
            self.jump_counter = 1
