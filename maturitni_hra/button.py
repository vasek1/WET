import pygame


class Button():
    def __init__(self,x,y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.height = 800
        self.width = 1200
        self.screen = pygame.display.set_mode((self.width, self.height))
    def draw(self):
        self.screen.blit(self.image,(self.rect.x, self.rect.y))