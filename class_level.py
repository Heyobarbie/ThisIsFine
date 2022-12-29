import pygame as pg
from support import import_csv_layout
from settings_for_tutorials import *
from class_Tile import Tile

class Level:
    def __init__(self, level_data, surface):
        self.display_surface= surface

        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

    def create_tile_group(self, layout, type):
        sprite_group =pg.sprite.Group()

        for row_index, row in enumerate(layout):
            for colunm_index, value in enumerate(row):
                if value != '-1':
                    x = colunm_index * tile_size
                    y = row_index * tile_size
                    
                    if type == 'terrain':
                        sprite = Tile(tile_size, x,y)
                        sprite_group.add(sprite)


        return sprite_group

    def run(self):
        self.terrain_sprites.draw(self.display_surface)