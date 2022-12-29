import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(topleft =(x,y))