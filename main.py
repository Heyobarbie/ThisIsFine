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
level = Level(level_0, sc)

# load a pic (if i want to make one colour transparent => .set_colorkey((*the color*)))
# making sprites for the hero
dog_surf = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\Sprites\Player\dog_up.png").convert_alpha()
dogg_surf = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\Sprites\Player\dog_right.png").convert_alpha()

dog_up = pg.transform.scale(dog_surf, (80, 100))
dog_down = pg.transform.flip(dog_up, True, True)

dog_right = pg.transform.scale(dogg_surf, (80, 100))
dog_left = pg.transform.flip(dog_right, True, False)

dog_rect = dog_up.get_rect(center=(W//2, H//2))

dog_sit = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\Sprites\Player\dog_sit.png").convert_alpha()
dog_sit = pg.transform.scale(dog_sit, (80, 120))
dog = dog_sit

sc.blit(dog_surf, dog_rect)

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

    caughtFireball(dog_rect)
    
    level.run()  #making level, adding sprites et.
    sc.blit(lifecount, (0,0))
    counter = pixelFont.render(str(LIVES), 2, BLACK) 
    sc.blit(counter, (25,10))
    
    sc.blit(dog, (dog_rect))   
    ballsGroup.draw(sc)
    pg.display.update()
    dog = dog_sit

    clock.tick(60)  # 60 frames per seconds
    ballsGroup.update(H)