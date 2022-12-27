import pygame as pg

class fireball(pg.sprite.Sprite):

    def __init__(self, x, speedball, surface, group):
        pg.sprite.Sprite.__init__(self)
        
        self.image = surface
        self.image = pg.transform.scale(self.image, (20, 40))
       
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speedball
        self.add(group)

    def update(self, *arg):
        if self.rect.y < (arg[0] - 20):
            self.rect.y += self.speed
        else:
            self.kill()
       
