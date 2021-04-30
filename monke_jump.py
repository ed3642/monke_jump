import pygame as pg
from pygame.locals import *
from monke import Monke


def main():
    pg.init()

    window = pg.display.set_mode((900, 350))
    pg.display.set_caption('Monke Jump')
    pg.mouse.set_visible(True)

    background = pg.Surface(window.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    #Initial bg draw onto window
    window.blit(background, (0, 0))
    pg.display.update()

    #load resources
    monke = Monke()

    allsprites = pg.sprite.RenderPlain((monke))
    clock = pg.time.Clock()

    keepRunning = True

    while keepRunning:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_SPACE:
                monke.jump_event()

        allsprites.update()
        window.blit(background, (0, 0))
        allsprites.draw(window)
        pg.display.update()

    pg.quit()


if __name__ == "__main__": main()