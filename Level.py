import pygame as pg
from support import *
from settings_for_tutorials import *
from Dog import *
from Generic import *
from pytmx.util_pygame import load_pygame
from begging_end import won

class Level:
    LIVES = 5
    isCurrentlyHit = []
    def __init__(self):
        self.sprite_group = CameraGroup()
        self.collision_group = pg.sprite.Group()
        self.damage_group = pg.sprite.Group()

        self.tmx_data = load_pygame("Resources/Maps/TryOut.tmx")
        self.create_tile_group()

        for _ in self.damage_group:
            self.isCurrentlyHit.append(False)

    def create_tile_group(self):
        self.sprite_group = CameraGroup()
        self.goal_group = pg.sprite.GroupSingle()

        for x_column, y_row, surface in self.tmx_data.get_layer_by_name('Floor').tiles():
                Tiles((x_column*tile_size, y_row*tile_size), surface ,self.sprite_group)

        for x_column, y_row, surface in self.tmx_data.get_layer_by_name('Walls').tiles():
                Tiles((x_column*tile_size, y_row*tile_size), surface, [self.sprite_group, self.collision_group])
        
        for x_column, y_row, surface in self.tmx_data.get_layer_by_name('Objects').tiles():
                Tiles((x_column*tile_size, y_row*tile_size), surface, [self.sprite_group, self.collision_group])
                    
        for obj in self.tmx_data.get_layer_by_name('Dog'):
            if obj.name == 'Dog':
                self.dog = Dog((obj.x, obj.y), self.sprite_group, self.collision_group)

        for obj in self.tmx_data.get_layer_by_name('Fire'):
            if obj.name == 'Fire':
                self.fire = Fire((obj.x, obj.y), surface, [self.sprite_group, self.damage_group])

        for obj in self.tmx_data.get_layer_by_name('Goal'):
            if obj.name == 'Goal':
                self.goal = Goal((obj.x, obj.y), surface, [self.sprite_group, self.goal_group])

        Tiles(
		position = (0,0),
		surface = pg.transform.scale(pg.image.load('Resources/background.jpg').convert_alpha(), (80, 120)),
		groups = self.sprite_group,
		z = LAYERS['background'])

    def check_win(self, surface):
        for goal in self.goal_group:
            if self.dog.rect.collidepoint(self.goal.rect.center):
                won(surface)

    def check_fire_collision(self):
        # using a list of collision states and checking with 'no collision' list , if one is true => looses only one life instead of instant death, otherwise counting down at each new collision check
        i = 0
        for ball in self.damage_group:
            if self.dog.rect.collidepoint(ball.rect.center):
                if (self.isCurrentlyHit[i] == False):
                    self.LIVES -= 1
                self.isCurrentlyHit[i] = True
            else:
                self.isCurrentlyHit[i] = False
            i += 1


    def run(self, surface):
        self.sprite_group.update()
        self.check_fire_collision()
        self.sprite_group.custom_draw(self.dog)
        self.check_win(surface)

class CameraGroup(pg.sprite.Group):
    ZoomFactor = 4
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = pg.math.Vector2()

        self.half_w = self.display_surface.get_size()[0] / 2
        self.half_h = self.display_surface.get_size()[1] / 2
        
        self.internal_surface_size = (W, H)#(1280*2, 720*2)
        self.internal_surface = pg.Surface(self.internal_surface_size, pg.SRCALPHA)
        self.internal_rect = self.internal_surface.get_rect(center = (self.half_w, self.half_h))
        self.internal_surface_vector = pg.math.Vector2(self.internal_surface_size)

    def custom_draw(self, dog):
    # def custom_draw(self, dog, ballsGroup, ballsOffsetX):

        self.offset.x = dog.rect.centerx - W/2
        self.offset.y = dog.rect.centery - H/2

        # global ballsOffsetX        
        # ballsOffsetX = 87 - dog.rect.centerx
        # ballsOffsetX = (ballsOffsetX + self.offset.x) - dog.rect.centerx
        # case inital: ballsOffsetX = 0 becasue do is in center and map is centered
        # case I move 20 to the left: offsetx needs to be 20
        # print("BOffSetX: " + str(ballsOffsetX) + "; dog.rect.centerx: " + str(dog.rect.centerx))
        self.internal_surface.fill(BLACK)

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset

                    self.internal_surface.blit(sprite.image, offset_rect) # self.display_surface.blit(sprite.image, offset_rect)
        
        # mb change x coord for each fireball in the group
        # ballsGroup.draw(self.internal_surface) # ballsGroup.draw(self.display_surface)

        scaled_surface = pg.transform.scale(self.internal_surface, self.internal_surface_vector*self.ZoomFactor)
        scaled_rect = scaled_surface.get_rect(center = (self.half_w, self.half_h))

        self.display_surface.blit(scaled_surface, scaled_rect)
