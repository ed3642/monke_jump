import pygame as pg
from pygame.locals import *
from load_resources import load_color_image
import random
from os import listdir
from os.path import isfile, join


class Obstacle(pg.sprite.Sprite):

    jump_count = 0
    jumps_in_row = 0

    img_folder_path = "./resources/images/champs"
    img_folder_size = len(listdir(img_folder_path))
    all_files = [f for f in listdir(img_folder_path) if isfile(join("./resources/images/champs", f))]

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_color_image(f'./images/champs/{self.chose_rand_file()}', -1)
        window = pg.display.get_surface()
        self.area = window.get_rect()
        self.rect.topleft = window.get_rect().right, 210
        self.original_pos = self.rect.left
        self.move = -10
        self.move_counter = 0
        self.move_delta = 10
        self.rand_gap = random.randint(1, 1000)
        self.collided = False

    def chose_rand_file(self):
        rand_img_index = random.randint(0, Obstacle.img_folder_size - 1)
        return Obstacle.all_files[rand_img_index]

    def update(self):
        if self.collided:
            Obstacle.jumps_in_row = 0
            self.rand_gap = random.randint(1, 1000)
            self.reset_object()
        elif self.move_counter:
            self.move_left()

    def move_left(self):
        self.move_counter += self.move_delta

        if self.is_offscreen():
            Obstacle.jump_count += 1
            Obstacle.jumps_in_row += 1
            self.reset_object()
            self.rand_gap = random.randint(1, 1000)

        self.rect = self.rect.move((self.move, 0))

    def is_offscreen(self):
        return self.rect.left < (0 - self.rect.width)
            
    def reset_object(self):
        new_img, new_img_rect = load_color_image(f'./images/champs/{self.chose_rand_file()}', -1)
        self.image.blit(new_img, (0,0))
        self.rect.left = self.original_pos + self.rand_gap
        self.move_counter = 0

    def move_event(self):
        if not self.move_counter:
            self.move_counter = 1

    