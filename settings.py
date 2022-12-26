import pygame as pg
from random import randint
W = 1280
H = 720

FPS = 60

SPEED = 5
SPEEDBALL = randint(1,5)

LIFES = 3

TILESIZE = 64

# define colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PINK = (255, 102, 255)
AQUA = (0, 204, 204)
GOLD = (255, 215, 0)



class fireball(pg.sprite.Sprite):

    def __init__(self, x, SPEEDBALL, filename ):
        pg.sprite.Sprite.__init__(self)
        
        self.image = pg.image.load(filename).convert_alpha()
        ball = pg.transform.scale(self.image, (20, 40))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = SPEEDBALL

    def update(self, *arg):
        if self.rect.y < (arg[0] - 20):
            self.rect.y += self.speed
        else:
            self.kill()
