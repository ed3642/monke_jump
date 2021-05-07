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

    #load resources
    hurt_sound = load_sound("./sounds/hurt.wav")

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
        else:
            text = font.render(f"Press \"Space\" to avoid brain dmg champs!"
            + f"                                Monke's dodges: {Obstacle.jump_count}!", True, (255,255,255))

        allsprites.update()
        allsprites.draw(window)
        bg_graphics.image.blit(pg.Surface((window.get_width(), 20)), (0,200))
        bg_graphics.image.blit(text, text_pos)
        pg.display.update()

    pg.quit()


if __name__ == "__main__": main()