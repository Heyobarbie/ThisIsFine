import pygame as pg
from random import randint
import sys
from settings import *
# import all the expansions for our module
pg.init()


sc = pg.display.set_mode((W, H))
pg.display.set_caption("THIS IS FINE")

clock = pg.time.Clock()  # delays the operations

x = W/2
y = H/2

# make a background
background_surf = pg.image.load(r"C:\Users\patri\study\Informatik\my game\back.jpg").convert()
sc.blit(background_surf, (0, 0))

# load a pic (if i want to make one colour transparent => .set_colorkey((*the color*)))
# making sprites for the hero
dog_surf = pg.image.load(r"C:\Users\patri\study\Informatik\my game\char.png").convert_alpha()

dogg_surf = pg.image.load(r"C:\Users\patri\study\Informatik\my game\my drawings\run_left.png")

dog_up = pg.transform.scale(dog_surf, (80, 100))
dog_down = pg.transform.flip(dog_up, True, True)

dog_left = pg.transform.scale(dogg_surf, (80, 100))
dog_right = pg.transform.flip(dog_left, True, False)
dog_rect = dog_up.get_rect(center=(W//2, H//2))

dog = dog_up

sc.blit(dog_surf, dog_rect)
pg.display.update()

# MAKING FIREBALLS

pg.time.set_timer(pg.USEREVENT, 3000) #timer 
b1 = fireball(randint(0,W), SPEEDBALL, r"C:\Users\patri\study\Informatik\my game\fireball.png")

while True:

    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.USEREVENT:
           sc.blit(b1.image, b1.rect)
           b1.update(H)
           pg.display.update()

    # loosing lifes

    #if (((fireball.rect.y == dog_rect.x) and (fireball.rect.x == dog_rect.x)) or (dog_rect.y == (H - 3))):

       # LIFES = LIFES - 1
    
    #if (LIFES == 0):
      #  print("dead")
        #you are dead

    # moves around

    keys = pg.key.get_pressed()

    if keys[pg.K_RIGHT]:
        dog = dog_right
        dog_rect.x += SPEED
        if (dog_rect.x > W - dog_rect.height):
            dog_rect.x = W - dog_rect.height

    if keys[pg.K_LEFT]:
        dog = dog_left
        dog_rect.x -= SPEED
        if (dog_rect.x < 0):
            dog_rect.x = 0

    if keys[pg.K_UP]:
        dog = dog_up
        dog_rect.y -= SPEED
        if (dog_rect.y < 0):
            dog_rect.y = 0

    if keys[pg.K_DOWN]:
        dog = dog_down
        dog_rect.y += SPEED
        if (dog_rect.y > H - dog_rect.height):
            dog_rect.y = H - dog_rect.height

    
    sc.blit(background_surf, (0, 0))
    sc.blit(dog, (dog_rect))   
    pg.display.update()

    clock.tick(60)  # 60 frames per seconds