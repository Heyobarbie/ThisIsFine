
W = 1280
H = 720

FPS = 60

SPEED = 3
LIVES = 5

vertical_tile_number = 60
horizonal_tile_number = 11
tile_size = 16

screen_height= vertical_tile_number * tile_size
screen_width = horizonal_tile_number * tile_size

# define colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PINK = (255, 102, 255)
AQUA = (0, 204, 204)
GOLD = (255, 215, 0)

LAYERS ={
    'background': 0,
    'floor': 1,
    'wall': 2,
    'objects':3,
    'dog': 4,
    'fire' : 5
}