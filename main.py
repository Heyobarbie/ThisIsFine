import pygame as pg
from random import randint
from settings import *
from fireballclass import fireball

pg.init()
sc = pg.display.set_mode((W, H))
pg.display.set_caption("THIS IS FINE")

lifecount = pg.image.load(r"C:\Users\patri\study\Informatik\my game\images\textbox.png").convert_alpha()
lifecount = pg.transform.scale(lifecount, (200,100))
pixelFont =pg.font.Font(r'C:\Users\patri\study\Informatik\my game\font\grand9k_pixel\Grand9K Pixel.ttf', 30)



clock = pg.time.Clock()  # delays the operations


# make a background
background = pg.image.load(r"C:\Users\patri\study\Informatik\my game\back.jpg").convert()


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

balls_info =({'path': 'fireball.png', 'damage': 1},
            {'path': 'fireball2.png', 'damage': 2})
balls_surf=[pg.image.load("images/"+info['path']).convert_alpha() for info in balls_info]

# balls_surf = []
# for image in balls_images:
#     path = "images/" + image
#     tmp_ball_surf = pg.image.load(path).convert_alpha

#     balls_surf.append(tmp_ball_surf)

balls =pg.sprite.Group()

def makeFireball (group):
    index = randint (0, len(balls_surf)-1)
    speedball = randint (2, 6)
    x = randint (20, W-20)
    return fireball(x, speedball, balls_surf[index], balls_info[index]['damage'], group)

def caughtFireball():
    global LIVES
    for ball in balls:
        if dog_rect.collidepoint(ball.rect.center):
            LIVES -= ball.damage
            ball.kill()

pg.time.set_timer(pg.USEREVENT, 2000) #timer 
makeFireball(balls)

while True:

    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.USEREVENT:
           makeFireball(balls)

    # loosing lifes by fireballs

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

    caughtFireball()
    sc.blit(background, (0, 0))
    sc.blit(lifecount, (0,0))
    counter = pixelFont.render( str(LIVES), 2, BLACK)
    sc.blit(counter, (25,10))
    
    sc.blit(dog, (dog_rect))   
    balls.draw(sc)
    pg.display.update()

    clock.tick(60)  # 60 frames per seconds
    balls.update(H)