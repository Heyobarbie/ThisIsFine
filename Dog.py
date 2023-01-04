import pygame as pg
from settings import *


class Dog(pg.sprite.Sprite):

    def __init__(self, position, surface, group) : ### group for camera, also in init
        super().__init__(group)

        self.image = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\Sprites\sit\dog_sit.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (80, 120))

        self.dog_right = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\Sprites\right\dog_right.png").convert_alpha()
        self.dog_right = pg.transform.scale(self.dog_right, (80, 100))
        self.dog_left = pg.transform.flip(self.dog_right, True, False)

        self.dog_top = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\Sprites\up\dog_top.png").convert_alpha()
        self.dog_top = pg.transform.scale(self.dog_top, (80, 100))
        self.dog_down = pg.transform.flip(self.dog_top, True, True)

    

        self.rect = self.image.get_rect(center = position)
        self.direction = pg.math.Vector2(0,0)
        self.pos = pg.math.Vector2(self.rect.center)
        self.z = LAYERS ['dog']
       
    
    
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
        


