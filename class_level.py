import pygame as pg
from support import *
from settings_for_tutorials import *
from class_Tile import *
from class_Dog import *

class Level:
    def __init__(self, level_data, surface):
        self.display_surface= surface
        self.world_shift = 0
        # repeat for different layers

        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

        dog_layout = import_csv_layout(level_data['dog'])
        self.player = pg.sprite.GroupSingle()
        self.dog_setup(dog_layout)
        self.goal = pg.sprite.GroupSingle 

    def dog_setup(self, layout):
          for row_index, row in enumerate(layout):
            for colunm_index, value in enumerate(row):
                if value == '0':
                    x = colunm_index * tile_size
                    y = row_index * tile_size





    def create_tile_group(self, layout, type):

        sprite_group =pg.sprite.Group()

        for row_index, row in enumerate(layout):
            for colunm_index, value in enumerate(row):
                if value != '-1':
                    x = colunm_index * tile_size
                    y = row_index * tile_size
                    
                    # terrain setup
                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphic(r"C:\Users\patri\study\Informatik\my game\sprites\64sprite_terrain.png")
                        tile_surface = terrain_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        
                    # dog setup
                    if type == 'D':
                        x = colunm_index * tile_size
                        y = row_index * tile_size
                        dog_sprite = Dog((x,y))

                    sprite_group.add(sprite)


        return sprite_group

    def run(self):
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)
        
        self.scroll_x()

        

    def scroll_x(self):
        dog = self.dog.sprite
        dog_x = dog.rect.centerx
        direction_x = dog.direction.x
        if dog_x < 200:
            self.world_shift = 8
            dog.speed = 0
