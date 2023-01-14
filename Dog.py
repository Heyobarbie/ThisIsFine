import pygame as pg
from settings import *


class Dog(pg.sprite.Sprite):

    def __init__(self, position, group, collision_group) : ### group for camera, also in init
        super().__init__(group)
        #for the dog animation
        self.import_assests()
        self.status = 'up'
        self.image = self.animations[self.status]

        self.image = pg.transform.scale(self.image, (14, 20))
        self.rect = self.image.get_rect(center = position)
        self.direction = pg.math.Vector2(0,0)
        self.position = pg.math.Vector2(self.rect.center)
        
        #for the collision
        self.collision_sprites = collision_group
        self.hitbox = (self.rect.copy().inflate((-2, -2)))
        self.z = LAYERS ['dog']
        
       
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

   
    def update(self):
        self.input_dog()
        self.move()
        self.image = self.animations[self.status]
        self.image = pg.transform.scale(self.image, (14, 20))

    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == 'horizontal':
                        if self.direction.x > 0: # moving right
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0: # moving left
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.position.x = self.hitbox.centerx

                    if direction == 'vertical':
                        if self.direction.y > 0: # moving down
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0: # moving up
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.position.y = self.hitbox.centery

    def move(self):
        #vector normalisation
        if self.direction.magnitude() > 0:
           self.direction = self.direction.normalize()

        self.position.x += self.direction.x * SPEED
        self.hitbox.centerx = round(self.position.x) 
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')

        self.position.y += self.direction.y * SPEED
        self.hitbox.centery = round(self.position.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')
            


