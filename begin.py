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



#upload a pic instead of a rectangle
#dog = pg.Surface((40,50))
#dog.fill(GOLD)
#rect=dog.get_rect(center=(W//2, H*2//3))
#sc.fill(BLACK)
#sc.blit(dog,(100, 50))
#pg.display.update

#make a background
background_surf = pg.image.load(r"C:\Users\patri\study\Informatik\my game\back.jpg").convert()
sc.blit(background_surf, (0,0))

#load a pic (if i want to make one colour transparent => .set_colorkey((*the color*)))
#redo the left and right

dog_surf = pg.image.load(r"C:\Users\patri\study\Informatik\my game\char.png").convert_alpha()
dogg_surf = pg.image.load(r"C:\Users\patri\study\Informatik\my game\left_right.png")
dog_up = dog_surf
dog_down = pg.transform.flip(dog_surf, 1, 0)
dog_left = dogg_surf
dog_right = pg.transform.rotate(dogg_surf, 90)
dog_rect = dog_surf.get_rect(center=(W//2, H//2))

dog=dog_up

sc.blit(dog_surf, dog_rect)
pg.display.update()

while True:



    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    keys = pg.key.get_pressed()


    if keys[pg.K_RIGHT]:
        dog = dog_right
        dog_rect.x += SPEED
        if (dog_rect.x < 0) :
            dog_rect.x = 0

    if keys[pg.K_LEFT]:
        dog = dog_left
        dog_rect.x -= SPEED
        if (dog_rect.x > W - dog_rect.height):
            dog_rect.x = W - dog_rect.height

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

    #sc.fill(BLACK)
    sc.blit(background_surf, (0,0))
    sc.blit(dog, (dog_rect))
    #pg.draw.rect(sc, GOLD, (x, y, 10, 20))
    pg.display.update()

    clock.tick(60) # 60 frames per seconds


