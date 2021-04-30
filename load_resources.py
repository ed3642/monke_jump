import os, sys
import pygame as pg
from pygame.locals import *


def load_colork_image(name, colorkey=None):
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

def load_norm_image(name):
    rel_path = os.path.join('resources', name)
    try:
        image = pg.image.load(rel_path)
    except pg.error as message:
        print('Error loading image: ', name)
        raise SystemExit(message)

    image = image.convert()

    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass

    if not pg.mixer:
        return NoneSound()
    fullname = os.path.join('resources', name)
    try:
        sound = pg.mixer.Sound(fullname)
    except pg.error as message:
        print('Cannot load sound:', fullname)
        raise SystemExit(message)
        
    return sound