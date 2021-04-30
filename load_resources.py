import os, sys
import pygame as pg
from pygame.locals import *

def load_image(name, colorkey=None):
    rel_path = os.path.join('resources', name)
    try:
        image = pg.image.load(rel_path)
    except pg.error as message:
        print('Error loading image: ', name)
        raise SystemExit(message)

    image = image.convert()
    
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def load_sound():
    pass