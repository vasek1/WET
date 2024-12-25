import pygame

class Camera(pygame.sprite.Group):
    def __init__(self, screen):
        super().__init__()
        self.display_surface = screen
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        self.zoom_scale = 3
        
        


    
        self.internal_surf_size = (500,300)
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_w,self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
        

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - (self.half_w / self.zoom_scale)
        self.offset.y = target.rect.centery - (self.half_h / self.zoom_scale)
        
        return (self.offset.x, self.offset.y)