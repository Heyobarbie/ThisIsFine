import pygame as pg
from random import randint

from settings import  W

class Fireball(pg.sprite.Sprite):    
    ballsInfoDict = ({'path': 'fireball.png', 'damage': 1},
                     {'path': 'fireball2.png', 'damage': 2})

    def __init__(self, group, surface):
        pg.sprite.Sprite.__init__(self, group) # call parent class constructor that handles the adding of the sprite to the group
        
        self.surfaceList=[pg.transform.scale(pg.image.load("Resources/Sprites/"+info['path']).convert_alpha(), (100, 140)) for info in self.ballsInfoDict]

        index = randint (0, len(self.surfaceList)-1) # generate a random index (currently just between 0 and 1)

        # self.image = pg.transform.scale(self.surfaceList[index], (100, 140))
        self.image = self.surfaceList[index]

        # self.damage= damage
    

        self.rect = self.image.get_rect(center=((randint (20, W-20)), 0))
        self.speed = randint (2, 6)
        #self.balls = pg.sprite.Group()
        
        self.damage = self.ballsInfoDict[index]['damage']
        self.display_surface = surface
        # self.display_surface.blit(self.image, self.rect)
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
        #return Fireball  (x, speedball, self.balls_surf[index],self.ballsInfoDict[index], group)

