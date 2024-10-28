import pygame

class Camera(pygame.sprite.Group):
 def __init__(self,screen):
        super().__init__()
        from map import Map
        from game import screen
        self.display_surface = screen
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        level_data = ("image/map/mapa.tmx")
       
        self.map = Map(screen,level_data)
        
def center_target_camera(self,target):
		self.offset.x = target.rect.centerx - self.half_w
		self.offset.y = target.rect.centery - self.half_h
def custom_draw(self):
            self.map.draw(self.display_surface,self.offset)
            for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
                  offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
                  self.internal_surf.blit(sprite.image,offset_pos)
   