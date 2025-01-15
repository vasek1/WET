import pygame
from settings import *
import player
from utility import get_image


class Monster1(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.position = position
        self.index = 0
        self.spritesheet = pygame.image.load("assets/monster/monster_spritesheet.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 0, 15, 16, 3)
        self.rect = self.image.get_rect(topleft=(position))
        self.direction = "Top"
        
   
    def animation(self):
        frame_count = 3
        self.index += 0.05
        if self.index >= frame_count:    
            self.index = 0
        self.image = get_image(self.spritesheet, int(self.index), 4 ,16 ,16, 5 ) 

    def update(self):
        self.animation()
        if self.rect.y <= 0:
            self.direction = "Bottom"
        elif self.rect.y >= screen_height - 50:
            self.direction = "Top"

        if self.direction == "Top":
            self.rect.y -= 5
        elif self.direction == "Bottom":
            self.rect.y += 5

    def  draw(self,screen):
        screen.blit(self.image, self.rect)