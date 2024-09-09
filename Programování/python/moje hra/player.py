import pygame
from screen import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.Rect((0,0,50,50))
        self.x = 100
        self.y = 200
        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] == True:
              self.move(-10, 0)
        elif key[pygame.K_RIGHT] == True:    
              self.move(10, 0)
        elif key[pygame.K_UP] == True:
              self.move(0, -10)
        elif key[pygame.K_DOWN] == True:
              self.move(0, 10)
    
         
         