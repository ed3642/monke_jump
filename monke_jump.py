import pygame as pg
from pygame.locals import *
from monke import Monke
from background_graphics import Background_Graphics
from obstacle import Obstacle
from load_resources import load_sound


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
    hurt_sound = load_sound("./sounds/hurt.wav")

    if not pg.font:
        print("Warning, fonts disabled")

    if pg.font:
        font = pg.font.Font(None, 20)
        text = font.render("Press \"Space\" to avoid brain ded champs!", 1, (10, 10, 10))
        text_pos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, text_pos)

    monke = Monke()
    obstacle = Obstacle()
    bg_graphics = Background_Graphics()

    allsprites = pg.sprite.RenderPlain((obstacle, monke))
    clock = pg.time.Clock()

    run = True

    while run:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_SPACE:
                monke.jump_event()
        
        obstacle.move_event()

        obstacle.collided = monke.rect.colliderect(obstacle.rect)

        if obstacle.collided:
            hurt_sound.play()

        allsprites.update()
        window.blit(background, (0, 0))
        allsprites.draw(window)
        pg.display.update()

    pg.quit()


if __name__ == "__main__": main()