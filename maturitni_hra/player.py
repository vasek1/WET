import pygame
from getimg import get_image 
from bar import *
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,camera_group):
        super().__init__() 
        self.x = 100
        self.y = 200
        self.spritesheet = pygame.image.load("image/entities/Player.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 0, 32, 31, 1) 
        self.speed = 1
        self.index = 0
        self.rect = self.image.get_rect(center = pos)
        self.camera_group = camera_group
        
    def animation(self, direction):
        frame_count = 6


        self.index += 0.3
        if self.index >= frame_count:
            self.index = 0

        self.image = get_image(self.spritesheet, int(self.index), direction, 32,31,1)

        
    def update(self):
        dx = 0
        dy = 0
        
        #muzu vymenit i za normalni if ale pak se bude panacek zrychlovat kdyz pujde diagonalne
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= self.speed
            self.animation(2)
        elif key[pygame.K_d]:
            dx += self.speed
            self.animation(4)
        elif key[pygame.K_w]:
            dy -= self.speed
            self.animation(5)
        elif key[pygame.K_s]:
            dy += self.speed
            self.animation(3)

        see1 = pygame.Rect(400, 571, 39, 34)
        

        #print(self.rect.x,self.rect.y)
        if self.rect.x < 319:
            self.rect.x = 319 + 1
        elif self.rect.x > 830:
            self.rect.x = 830 - 1
        
        if self.rect.y < 210:
            self.rect.y = 210 + 1
        elif self.rect.y > 744:
            self.rect.y = 744 -1

        self.rect.x += dx 
        self.rect.y += dy 
        
        #print(self.rect.x,self.rect.y)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        