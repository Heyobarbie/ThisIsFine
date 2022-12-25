import pygame as pg
import sys
from settings import *
#import all the expansions for our module
pg.init()


sc = pg.display.set_mode((W, H)) 
pg.display.set_caption("THIS IS FINE")

clock = pg.time.Clock() # delays the operations

x = W/2
y = H/2


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
    pg.draw.rect(sc, GOLD, (x, y, 10, 20))
    pg.display.update()

    clock.tick(60) # 60 frames per seconds
