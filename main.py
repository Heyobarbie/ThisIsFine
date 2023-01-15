import pygame as pg
from random import randint
from settings import *
from Fireball import *
from Level import *
from game_data import level_0
from Dog import *
from begging_end import *

pg.init()
sc = pg.display.set_mode((W, H))
pg.display.set_caption("THIS IS FINE")

lifecount = pg.image.load("Resources/textbox.png").convert_alpha() # load the beckground for life count
lifecount = pg.transform.scale(lifecount, (200,100)) # make it smaller
pixelFont =pg.font.Font('Resources/Fonts/Grand9KPixel.ttf', 30) # load the font for count

clock = pg.time.Clock()  # delays the operations
level = Level() # prepare the level

ballsGroup = pg.sprite.Group()

pg.time.set_timer(pg.USEREVENT, 2000) #timer 
Fireball(ballsGroup)

begining(sc) # animation in the beginning
pg.display.update()
GODMODE = False 

while True:
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif keys[pg.K_3]:
            if GODMODE:
                GODMODE = False
            else:
                GODMODE = True
        elif keys[pg.K_PLUS]:
            if GODMODE:
                CameraGroup.ZoomFactor+=0.05
        elif keys[pg.K_MINUS]:
            if GODMODE:
                CameraGroup.ZoomFactor-=0.05
        elif event.type == pg.USEREVENT:
           Fireball(ballsGroup)
    if (level.LIVES == 0) or (level.LIVES < 0) : # dying mechanism
        game_over(sc)
    # moves around
    
    level.run(sc)  # making level, adding sprites,charcter movin et.
    sc.blit(lifecount, (0,0))
    counter = pixelFont.render(f"{str(level.LIVES)} Lives", 2, BLACK) 
    sc.blit(counter, (25,10))
      
    ballsGroup.draw(sc)
    pg.display.update()

    clock.tick(60)  # 60 frames per seconds
    ballsGroup.update(H)