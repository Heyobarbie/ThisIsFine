import pygame as pg
from settings import *


class Dog(pg.sprite.Sprite):

    def __init__(self, position, surface, group) : ### group for camera, also in init
        super().__init__(group)

        self.import_assests()
        self.status = 'up'
        self.image = self.animations[self.status]
        self.image = pg.transform.scale(self.image, (80, 120))

        # self.image = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\Sprites\Player\dog_sit.png").convert_alpha()
        # self.image = pg.transform.scale(self.image, (80, 120))

        # self.dog_right = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\Sprites\Player\dog_right.png").convert_alpha()
        # self.dog_right = pg.transform.scale(self.dog_right, (80, 100))
        # self.dog_left = pg.transform.flip(self.dog_right, True, False)

        # self.dog_top = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\Sprites\Player\dog_up.png").convert_alpha()
        # self.dog_top = pg.transform.scale(self.dog_top, (80, 100))
        # self.dog_down = pg.transform.flip(self.dog_top, True, True)

    

        self.rect = self.image.get_rect(center = position)
        self.direction = pg.math.Vector2(0,0)
        self.position = pg.math.Vector2(self.rect.center)
        self.z = LAYERS ['dog']
        self.hitbox = self.rect.copy().inflate((-100, -70))
       
    def import_assests(self):
        self.animations = { 'up': (), 'down': (), 'right': (), 'left': (), 'sit': ()}
        for animation in self.animations.keys():
            full_path = 'Resources/Sprites/Player/dog_' + animation + '.png'
            self.animations[animation] = pg.image.load(full_path).convert_alpha()
    
    def input_dog(self):
        keys = pg.key.get_pressed()

        self.status= 'sit'
        if keys[pg.K_UP]:
            self.status = 'up'
            self.direction.y = - SPEED
        elif keys[pg.K_DOWN]:
            self.status = 'down'
        
            self.direction.y = SPEED
        else:
            self.direction.y = 0



        if keys[pg.K_RIGHT]:
            self.status = 'right'
            
            self.direction.x = SPEED
        elif keys[pg.K_LEFT]:
            self.status = 'left'
            
            self.direction.x = -SPEED
        else:
            self.direction.x = 0

    def move(self):
        #vector normalisation
        if self.direction.magnitude() > 0:
           self.direction = self.direction.normalize()

        self.position.x += self.direction.x * SPEED
        self.hitbox.centerx = round(self.position.x) 
        self.rect.centerx = self.hitbox.x

        self.position.y += self.direction.y * SPEED
        self.hitbox.centery = round(self.position.y)
        self.rect.centery = self.hitbox.y
        
    def update(self):
        self.input_dog()
        self.move()
        self.image = self.animations[self.status]
        self.image = pg.transform.scale(self.image, (80, 120))
        


