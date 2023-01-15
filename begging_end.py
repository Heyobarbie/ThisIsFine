import sys
import pygame as pg
from settings import *

def begining(surface):
    # animation in the beginning
    surface.fill(BLACK)
    animations = [1,2,3,4,5,6,7]
    for animation in animations:
      full_path = "../Ideas, PotentialResources/AnimationBeggining/" + str(animation) + ".jpg"
      animation = animation + 1
      image =  pg.image.load(full_path).convert_alpha()
      image = pg.transform.scale(image, (W,H))
      surface.blit(image, (0,0))
      pg.display.update()
      pg.time.delay (1000)
    
def won(surface): # shows animations for successful ending the game
  surface.fill(BLACK)

  animations = [1,2,3,4,5]
  x = 700
  i = 0
  x2 = 1000
  for animation in animations: # to fix
      full_path = "../Ideas, PotentialResources/won/" + str(animation) + ".jpg"
      # animation = animation + 1
      image =  pg.image.load(full_path).convert_alpha()
      image = pg.transform.scale(image, (W,H))
      dog = pg.Surface((14,17))
      dog.fill(GOLD)

      truck = pg.image.load('Resources/Sprites/truck.png').convert_alpha()
      truck = pg.transform.scale(truck, (200,80))

      surface.blit(image, (0,0))
      surface.blit(dog, (x,370))
      if animation == 1:
        for i in range(20):
          x = x + 7
          surface.blit(image, (0,0))
          surface.blit(dog,(x,370))
          pg.display.update()
          pg.time.delay(200)        
        
        surface.blit(truck, ((x2, 600)))

        for i in range(40):
          x2 = x2 - 7
          surface.blit(image, (0,0))
          surface.blit(dog,(x,370))
          surface.blit(truck, (x2, 600))
          pg.display.update()
          pg.time.delay(100)


      surface.blit(truck, (x2, 600))
      pg.display.update()
      pg.time.delay (1000)
    


def game_over(surface):
    #text for the game over
    #game_over_text = pixelFont.render('GAME OVER', 9, WHITE) 
    #score_text = pixelFont.render('your time is') #pu here a countdown
    surface.fill(BLACK)
    game_over_back = pg.image.load('Resources/game_over_bakcground.jpg').convert_alpha()
    game_over_back = pg.transform.scale(game_over_back,(W, H))
    surface.blit(game_over_back, (0,0))
    #sc.blit(game_over_text, (W/2 -game_over_text.get_width()/2, H/7 ))
    
    pg.display.update()
    pg.time.delay(10000)
    pg.quit()
    sys.exit()