import pygame as pg
from settings import *

class Generic(pg.sprite.Sprite):
    def __init__(self, position, surface, groups, z = LAYERS['background']):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft = position)
        self.z = z
