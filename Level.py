import pygame as pg
from support import *
from settings_for_tutorials import *
#from Tile import *
from Dog import *
from Generic import *
from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.sprite_group = CameraGroup()
        self.collision_group = pg.sprite.Group()
        self.create_tile_group()

        #terrain_layout = import_csv_layout(level_data['terrain'])
        #self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')


        # self.goal = pg.sprite.GroupSingle()
        # self.player = pg.sprite.GroupSingle()
        #dog_layout = import_csv_layout(level_data['dog'])
        #self.dog_setup(dog_layout)


    # def dog_setup(self, layout):

    #     for row_index, row in enumerate(layout):
    #         for colunm_index, value in enumerate(row):
    #                 x = colunm_index * tile_size
    #                 y = row_index * tile_size

    #                 if value == '0':
    #                     self.dog = Dog((x, y), self.display_surface, self.sprite_group)

                        

    def create_tile_group(self):
        tmx_data = load_pygame(r"C:\Users\patri\study\Informatik\MyGame\Ideas, PotentialResources\tiles\TryOut.tmx")

        self.sprite_group = CameraGroup()
        #Tiles(position = (0,0), surface = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\background.jpg").convert_alpha(), groups = self.sprite_group, z = LAYERS['background'])

        for x_column, y_row, surf in tmx_data.get_layer_by_name('Floor').tiles():
                Tiles((x_column*tile_size, y_row*tile_size), surf,self.sprite_group)

        for x_column, y_row, surf in tmx_data.get_layer_by_name('Walls').tiles():
                Tiles((x_column*tile_size, y_row*tile_size), surf, [self.sprite_group, self.collision_group])
        
        for x_column, y_row, surf in tmx_data.get_layer_by_name('Objects').tiles():
                Tiles((x_column*tile_size, y_row*tile_size), surf, [self.sprite_group, self.collision_group])
                    
        for obj in tmx_data.get_layer_by_name('Dog'):
            if obj.name == 'Dog':
                self.dog = Dog((obj.x, obj.y), self.sprite_group, self.collision_group)
        Tiles(
		position = (0,0),
		surface = pg.transform.scale(pg.image.load('Resources/background.jpg').convert_alpha(), (80, 120)),
		groups = self.sprite_group,
		z = LAYERS['background'])

    def run(self):
        self.display_surface.fill(BLACK)
        self.sprite_group.update()
        self.sprite_group.custom_draw(self.dog)
        #make an overlay wit lives and such timer

class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = pg.math.Vector2()

    def custom_draw(self, dog):
        self.offset.x = dog.rect.centerx - W/2
        self.offset.y = dog.rect.centery - H/2

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset

                    self.display_surface.blit(sprite.image, offset_rect)
