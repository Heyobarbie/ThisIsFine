import pygame as pg
import sys
from settings import *
#import all the expansions for our module
pg.init()


sc = pg.display.set_mode((W, H)) # or mb pg.FULLSCREEN
pg.display.set_caption("Welcome to hell")

clock = pg.time.Clock() # delays the operations

x = W/2
y = H/2





surf.fill(AQUA)

x, y = 0, 0



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


    sc.fill(BLACK)
    sc.blit(surf, (x,y))
    pg.display.update()

    clock.tick(FPS) # 60 frames per seconds
