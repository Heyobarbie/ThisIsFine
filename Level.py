import pygame as pg
from support import *
from settings_for_tutorials import *
from Dog import *
from Generic import *
from pytmx.util_pygame import load_pygame
from begging_end import won

class Level:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.sprite_group = CameraGroup()
        self.collision_group = pg.sprite.Group()

        self.tmx_data = load_pygame(r"C:\Users\patri\study\Informatik\MyGame\Ideas, PotentialResources\tiles\TryOut.tmx")
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

        self.sprite_group = CameraGroup()
        #Tiles(position = (0,0), surface = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\GameRepo\Resources\background.jpg").convert_alpha(), groups = self.sprite_group, z = LAYERS['background'])

        for x_column, y_row, surface in self.tmx_data.get_layer_by_name('Floor').tiles():
                Tiles((x_column*tile_size, y_row*tile_size), surface ,self.sprite_group)

        for x_column, y_row, surface in self.tmx_data.get_layer_by_name('Walls').tiles():
                Tiles((x_column*tile_size, y_row*tile_size), surface, [self.sprite_group, self.collision_group])
        
        for x_column, y_row, surface in self.tmx_data.get_layer_by_name('Objects').tiles():
                Tiles((x_column*tile_size, y_row*tile_size), surface, [self.sprite_group, self.collision_group])
                    
        for obj in self.tmx_data.get_layer_by_name('Dog'):
            if obj.name == 'Dog':
                self.dog = Dog((obj.x, obj.y), self.sprite_group, self.collision_group)

        Tiles(
		position = (0,0),
		surface = pg.transform.scale(pg.image.load('Resources/background.jpg').convert_alpha(), (80, 120)),
		groups = self.sprite_group,
		z = LAYERS['background'])

    def check_win(self):
        if pg.sprite.spritecollide(self.dog, self.goal, False):
            won()



    # def fire_making(self):
    #     clock = pg.time.Clock()
    #     time_count = 0
    #     time_count = clock.tick()
    #     if type(time_count/1000)== int:
    #         x = randint(0, screen_width)
    #         y = randint(0,screen_height)
    #         surface = pg.image.load(r"C:\Users\patri\study\Informatik\MyGame\Ideas, PotentialResources\fire\1.png")
    #         Fire((x,y), surface, [self.sprite_group, self.collision_group] ) 


    def run(self):
        self.display_surface.fill(BLACK)
        self.sprite_group.update()
        #self.fire_making()
        self.sprite_group.custom_draw(self.dog)





        # self.display_surface = pg.transform.scale_by(self.display_surface,1)


        #make an overlay wit lives and such timer

class CameraGroup(pg.sprite.Group):
    ZoomFactor = 1
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = pg.math.Vector2()

        self.half_w = self.display_surface.get_size()[0] / 2
        self.half_h = self.display_surface.get_size()[1] / 2
        
        self.internal_surface_size = (1280, 720)#(1280*2, 720*2)
        self.internal_surface = pg.Surface(self.internal_surface_size, pg.SRCALPHA)
        self.internal_rect = self.internal_surface.get_rect(center = (self.half_w, self.half_h))
        self.internal_surface_vector = pg.math.Vector2(self.internal_surface_size)

    def custom_draw(self, dog):
        self.offset.x = dog.rect.centerx - W/2
        self.offset.y = dog.rect.centery - H/2



        self.internal_surface.fill(BLACK)

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset

                    self.internal_surface.blit(sprite.image, offset_rect) # self.display_surface.blit(sprite.image, offset_rect)
        
        scaled_surface = pg.transform.scale(self.internal_surface, self.internal_surface_vector*self.ZoomFactor)
        scaled_rect = scaled_surface.get_rect(center = (self.half_w, self.half_h))

        self.display_surface.blit(scaled_surface, scaled_rect)
