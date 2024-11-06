import pygame

class Camera(pygame.sprite.Group):
    def __init__(self, screen):
        super().__init__()
        self.display_surface = screen
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        
    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w 
        self.offset.y = target.rect.centery - self.half_h 
        return (self.offset.x, self.offset.y)
