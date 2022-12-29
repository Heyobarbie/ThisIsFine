import pygame as pg
from settings import *
from settings_for_tutorials import *
from class_level import Level
from game_data import level_0
#import all the expansions for our module
pg.init()


sc = pg.display.set_mode((screen_width, screen_height)) # or mb pg.FULLSCREEN
pg.display.set_caption("This is fine")

clock = pg.time.Clock() # delays the operations
level = Level(level_0, sc)


x, y = W//2, H//2
surf = pg.Surface((20,20))
surf.fill(PINK)
sc.blit(surf,(50,50))
pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    

    keys = pg.key.get_pressed()

    if keys[pg.K_RIGHT]:
     x += SPEED
    if keys[pg.K_LEFT]:
     x -= SPEED
    if keys[pg.K_UP]:
     y -= SPEED
    if keys[pg.K_DOWN]:
     y += SPEED


    level.run()
    sc.blit(surf, (x,y))
    pg.display.update()

    clock.tick(FPS) # 60 frames per seconds
