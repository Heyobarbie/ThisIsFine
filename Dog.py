import pygame as pg
from settings import *

class Dog(pg.sprite.Sprite):

    def __init__(self, position) : ### group for camera, also in init
        super().__init__()

        self.image = pg.Surface((32,64))
        self.image.fill(PINK)

        #self.right = pg.image.load(r"C:\Users\patri\study\Informatik\my game\my drawings\dog_right.png").convert_alpha()
        #self.top = pg.image.load(r"C:\Users\patri\study\Informatik\my game\char.png").convert_alpha()

        self.rect = self.image.get_rect(center = position)
        self.direction = pg.math.Vector2(0,0)
        self.pos = pg.math.Vector2(self.rect.center)
        self.speed = SPEED
       
        #self.left = pg.transform.scale(self.right, (100,120))
        #self.down = pg.transform.scale(self.top, (100,120))


    
    def input_dog(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            self.direction.y = - SPEED
        elif keys[pg.K_DOWN]:
            self.direction.y = SPEED
        else:
            self.direction.y = 0

        if keys[pg.K_RIGHT]:
            self.direction.x = SPEED
        elif keys[pg.K_LEFT]:
            self.direction.x = -SPEED
        else:
            self.direction.x = 0
        
    def update(self):
        self.input_dog()
        self.rect.x = self.rect.x + self.direction.x
        self.rect.y = self.rect.y + self.direction.y
        


