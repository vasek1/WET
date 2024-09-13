import pygame


class Button():
    def __init__(self,x,y, image,scale):
        self.width1 = 46
        self.height1 = 22
        self.image = pygame.transform.scale(image,(int(self.width1*scale), int(self.height1*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.width = 1200
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
    def draw(self):
        self.screen.blit(self.image,(self.rect.x, self.rect.y))
    def click(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False