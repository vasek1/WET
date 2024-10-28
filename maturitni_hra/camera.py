import pygame
from player import Player
from map import *

class Camera(pygame.sprite.Group):
 def __init__(self, display_surface):
        super().__init__()
        self.display_surface = display_surface
        self.offset = pygame.math.Vector2(0,0)
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        self.map  = map
def center_target_camera(self,target):
		self.offset.x = target.rect.centerx - self.half_w
		self.offset.y = target.rect.centery - self.half_h
def custom_draw(self):
      self.map.draw(self.offset)
      
      for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)   