import pygame as pg
from settings import *
#from settings_for_tutorials import *
from class_level import *
from game_data import level_0
from Dog import *
#import all the expansions for our module
pg.init()

sc = pg.display.set_mode((1200, 800)) # or mb pg.FULLSCREEN
pg.display.set_caption("This is fine")
background = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\back.jpg").convert()

clock = pg.time.Clock() # delays the operations
level = Level(level_0, sc)

pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    sc.fill(BLACK)
    sc.blit(background, (0,0))
    level.run()
    pg.display.update()

    clock.tick(FPS) # 60 frames per seconds
