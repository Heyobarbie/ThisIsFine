import pygame as pg
from random import randint

from settings import  W

class Fireball(pg.sprite.Sprite):
    display_surface = pg.display.get_surface()
    BallsInfoDict = ({'path': 'fireball.png', 'damage': 1},
                     {'path': 'fireball2.png', 'damage': 2})
    surfaceList=[pg.image.load("Resources/Sprites/"+info['path']).convert_alpha() for info in BallsInfoDict]
    

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        
        index = randint (0, len(self.surfaceList)-1)


        self.image = pg.transform.scale(self.surfaceList[index], (100, 140))
        
        # self.damage= damage
    

        self.rect = self.image.get_rect(center=((randint (20, W-20)), 0))
        self.speed = randint (2, 6)
        #self.balls = pg.sprite.Group()
        
        self.damage = self.BallsInfoDict[index]['damage']
        self.display_surface.blit(self.image, self.rect)
        #self.add(self.balls) 

        
    def update(self, *arg):
        if self.rect.y < (arg[0] - 20):
            self.rect.y += self.speed
        else:
            self.kill()
    

    #def makeFireball (self):
        # index = randint (0, len(self.balls_surf)-1)
        # speedball = randint (2, 6)
        # x = randint (20, W-20)
        #return Fireball  (x, speedball, self.balls_surf[index],self.BallsInfoDict[index], group)

