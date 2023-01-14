import pygame as pg
from settings import *

class Tiles(pg.sprite.Sprite):
    def __init__(self, position, surface, groups, z = LAYERS['floor']):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft = position)
        self.z = z
        self.hitbox = self.rect.copy().inflate(-2, -3)

class Wall(Tiles):
    def __init__(self, position, surface, groups, ):
        super().__init__(position,surface, groups)
        self.z = LAYERS['wall']
        self.hitbox = self.rect.copy().inflate(-2, -3)

class Objects(Tiles):
    def __init__(self, position, surface, groups, ):
        super().__init__(position, groups)
        self.image = surface
        self.z = LAYERS['objects']

