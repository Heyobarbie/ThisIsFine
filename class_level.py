import pygame as pg
from support import *
from settings_for_tutorials import *
from class_Tile import *
from Dog import *

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = 3
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
                    x = colunm_index * tile_size
                    y = row_index * tile_size

                    if value == '0':
                        dog = Dog((x,y), self.display_surface)
                        self.player.add(dog)

    def create_tile_group(self, layout, type):

        self.sprite_group =pg.sprite.Group()

        for row_index, row in enumerate(layout):
            for colunm_index, value in enumerate(row):
                if value != '-1':
                    x = colunm_index * tile_size
                    y = row_index * tile_size
                    
                    # terrain setup
                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphic(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\sprites\64sprite_terrain.png")
                        tile_surface = terrain_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                    

                    self.sprite_group.add(sprite)


        return self.sprite_group

    def run(self):
        self.sprite_group.draw(self.display_surface)
        self.sprite_group.update(self.world_shift)
        
        self.player.update()
        self.player.draw(self.display_surface)
        
        
