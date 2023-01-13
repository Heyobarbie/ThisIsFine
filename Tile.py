import pygame as pg
from settings import *

class Tile(pg.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.rect = self.image.get_rect(topleft =(x,y))
        self.hitbox = self.rect.copy().inflate(-self.rect.width *0.2, -self.rect.height * 0.75)


    def update(self):
        self.rect.y += 0

class StaticTile(Tile):
    def __init__(self, size, x, y, surface, z = LAYERS['room']):
        super().__init__(size,x,y)
        self.image = surface
        self.rect = self.image.get_rect(topleft =(x,y))
        self.hitbox = self.rect.copy().inflate(-self.rect.width *0.2, -self.rect.height * 0.75)
        self.z = z
        