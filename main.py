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

lifecount = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\textbox.png").convert_alpha()
lifecount = pg.transform.scale(lifecount, (200,100))
pixelFont =pg.font.Font(r'C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\Fonts\Grand9KPixel.ttf', 30)

clock = pg.time.Clock()  # delays the operations
level = Level()
#sc.blit(dog_surf, dog_rect)

ballsGroup = pg.sprite.Group()

def caughtFireball(dog_rect):
    global LIVES
    for ball in ballsGroup:
        if dog_rect.collidepoint(ball.rect.center): # TODO CHECK
            LIVES -= ball.damage
            ball.kill()



pg.time.set_timer(pg.USEREVENT, 2000) #timer 
Fireball(ballsGroup)

#begining(sc)
pg.display.update()
GODMODE = False

while True:
    keys = pg.key.get_pressed()
    
    
    #if keys[pg.K_SPACE]:
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
    if (LIVES == 0) or (LIVES < 0) :
        game_over(sc)
    # moves around

   # caughtFireball(dog_rect)
    
    level.run()  #making level, adding sprites et.
    sc.blit(lifecount, (0,0))
    counter = pixelFont.render(str(LIVES), 2, BLACK) 
    sc.blit(counter, (25,10))
      
    ballsGroup.draw(sc)
    pg.display.update()

    clock.tick(60)  # 60 frames per seconds
    ballsGroup.update(H)