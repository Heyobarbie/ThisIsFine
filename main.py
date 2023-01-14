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
        if dog_rect.collidepoint(ball.rect.center):
            LIVES -= ball.damage
            ball.kill()



pg.time.set_timer(pg.USEREVENT, 2000) #timer 
Fireball(ballsGroup,sc)
pg.display.update()

while True:
    keys = pg.key.get_pressed()
    #if keys[pg.K_SPACE]:
    #begining(sc)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.USEREVENT:
           Fireball(ballsGroup, sc)
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