import pygame as pg
from pygame.locals import *
from monke import Monke
from background_graphics import Background_Graphics
from obstacle import Obstacle
from load_resources import load_sound
import time


def game():
    pg.init()

    window = pg.display.set_mode((900, 350))
    pg.display.set_caption('Monke Jump')
    pg.mouse.set_visible(True)

    #load resources
    gp_theme = load_sound("./sounds/gp_theme.mp3")
    hurt_sound = load_sound("./sounds/hurt.wav")
    three_in_a_row = load_sound("./sounds/three_in_a_row.mp3")

    if not pg.font:
        print("Warning, fonts disabled")
    else:
        font = pg.font.Font(None, 30)
        text = font.render("", True, (255, 255, 255))
        text_pos = text.get_rect(topleft=(20,200))

    monke = Monke()
    obstacle = Obstacle()
    bg_graphics = Background_Graphics()

    allsprites = pg.sprite.RenderPlain((bg_graphics, obstacle, monke))
    clock = pg.time.Clock()

    run = True

    gp_theme.play()

    while run:
        clock.tick(60 + Obstacle.jump_count * 2)

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
            monke.lives -= 1
            if monke.lives <= 0:
                text = font.render(f"YOUR BOOSTED! Your score: {Obstacle.jump_count} qq", True, (255,255,255))
                run = False
        else:
            if Obstacle.jumps_in_row >= 3: 
                Obstacle.jumps_in_row = 0
                three_in_a_row.play()
            ints = (monke.lives * -1) + 10
            text = font.render(f"Press \"Space\". Double digit ints = gg"
            + f"               Monke's dodges: {Obstacle.jump_count}!"
            + f"               Ints: {ints}",
            True, (255,255,255))

        update_tick(allsprites, bg_graphics, window, text, text_pos)


    update_tick(allsprites, bg_graphics, window, text, text_pos)

    time.sleep(2)
    pg.quit()

def update_tick(allsprites, bg_graphics, window, text, text_pos):
    allsprites.update()
    allsprites.draw(window)
    bg_graphics.image.blit(pg.Surface((window.get_width(), 20)), (0,200))
    bg_graphics.image.blit(text, text_pos)
    pg.display.update()