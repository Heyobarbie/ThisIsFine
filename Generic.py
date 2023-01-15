import pygame as pg
from settings import *

class Tiles(pg.sprite.Sprite):
    def __init__(self, position, surface, groups, z = LAYERS['floor']):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft = position)
        self.z = z
        self.hitbox = self.rect.copy().inflate(-self.rect.width*0.2, -self.rect.height*0.7)

class Wall(Tiles):
    def __init__(self, position, surface, groups):
        super().__init__(position,surface, groups)
        self.z = LAYERS['wall']
        self.hitbox = self.rect.copy().inflate(-self.rect.width*0.3, -self.rect.height*0.8)

class Objects(Tiles):
    def __init__(self, position, surface, groups):
        super().__init__(position, groups)
        self.image = surface
        self.z = LAYERS['objects']

class Fire(Tiles):
    def __init__(self, position, surface, groups):
        super().__init__(position, surface, groups)
        self.image = pg.image.load("Resources/Sprites/fireball.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (24,20))
        self.rect = self.image.get_rect(center = position)
        self.hitbox = self.rect.copy().inflate(-self.rect.width*0.3, -self.rect.height*0.8)
        self.z = LAYERS['fire']

