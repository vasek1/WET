import pygame


class Button():
    def __init__(self,x,y, image,scale,width1,height1):
        self.width1 = width1
        self.height1 = height1
        self.image = pygame.transform.scale(image, (int(self.width1 * scale), int(self.height1 * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.width = 1200
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
    def click(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False

           