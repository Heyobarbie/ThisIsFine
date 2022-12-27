import pygame as pg
import random

class fireball(pg.sprite.Sprite):

    def __init__(self, x, speedball, filename):

        pg.sprite.Sprite.__init__(self)
        
        self.image = pg.image.load(filename).convert_alpha()
        ball = pg.transform.scale(self.image, (20, 40))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speedball

    def update(self, *arg):
        if self.rect.y < (arg[0] - 20):
            self.rect.y += self.speed
        else:
            self.kill()
