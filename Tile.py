import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pg.Surface((size, size))
        
        self.rect = self.image.get_rect(topleft =(x,y))

    def update(self):
        self.rect.y += -2

class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size,x,y)
        self.image = surface
        