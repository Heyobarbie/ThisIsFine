import pygame as pg
from support import *
from settings_for_tutorials import *
from Tile import *
from Dog import *
from sprites import Generic

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = -2

        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')


        self.goal = pg.sprite.GroupSingle()
        self.player = pg.sprite.GroupSingle()
        dog_layout = import_csv_layout(level_data['dog'])
        self.dog_setup(dog_layout)

        

    def dog_setup(self, layout):

        
        for row_index, row in enumerate(layout):
            for colunm_index, value in enumerate(row):
                    x = colunm_index * tile_size
                    y = row_index * tile_size

                    if value == '0':
                        dog = Dog((640,320), self.display_surface, self.sprite_group)
                        

    def create_tile_group(self, layout, type):

        self.sprite_group = CameraGroup()
        Generic(position = (0,0), surface = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\background.jpg").convert_alpha(), groups = self.sprite_group, z = LAYERS['background'])

        for row_index, row in enumerate(layout):
            for colunm_index, value in enumerate(row):
                if value != '-1':
                    x = colunm_index * tile_size
                    y = row_index * tile_size
                    
                    # terrain setup
                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphic(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\Sprites\64sprite_terrain.png")
                        tile_surface = terrain_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    self.sprite_group.add(sprite)


        return self.sprite_group

    def run(self):
        self.sprite_group.custom_draw()
        self.sprite_group.update()

class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
    def custom_draw(self):
        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                   self.display_surface.blit(sprite.image, sprite.rect)
            
