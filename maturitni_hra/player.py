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
        self.speed = 0.8
        self.index = 0
        self.rect = self.image.get_rect(center = pos)
        self.camera_group = camera_group
        self.wood = 0
        self.fire = False
        self.can_kill = False
        self.cut_trees = False
        self.float_x = self.rect.x
        self.float_y = self.rect.y
    def animation(self, direction):
        frame_count = 6


        self.index += 0.3
        if self.index >= frame_count:
            self.index = 0

        self.image = get_image(self.spritesheet, int(self.index), direction, 32,31,1)
    def animation2(self, direction):
        frame_count = 4


        self.index += 0.3
        if self.index >= frame_count:
            self.index = 0

        self.image = get_image(self.spritesheet, int(self.index), direction, 32,32,1)
    def animation3(self, direction):
        frame_count = 2


        self.index += 0.1
        if self.index >= frame_count:
            self.index = 0

        self.image = get_image(self.spritesheet, int(self.index), direction, 32,32,1)

    
        
    def update(self):
        dx = 0
        dy = 0
       
        key = pygame.key.get_pressed()
        if self.fire == False:
          if not self.cut_trees:
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
        if self.fire == True:
          if not self.cut_trees:
            if key[pygame.K_a]:
                dx -= self.speed
                self.animation(6)
            elif key[pygame.K_d]:
                dx += self.speed
                self.animation(8)
            elif key[pygame.K_w]:
                dy -= self.speed
                self.animation(9)
            elif key[pygame.K_s]:
                dy += self.speed
                self.animation(7)
        if key[pygame.K_k]:
            self.animation2(10)
            self.can_kill = True
        elif key[pygame.K_b] and self.wood >= 5:
            self.fire = True
            
        elif key[pygame.K_j]:
            self.animation3(11)
            self.cut_trees = True
            self.wood += 0.01
        else: 
            self.cut_trees = False
            
            
        
        self.float_x += dx
        self.float_y += dy

        
        if self.float_x < 319:
            self.float_x = 319 + 1
        elif self.float_x > 830:
            self.float_x = 830 - 1

        if self.float_y < 210:
            self.float_y = 210 + 1
        elif self.float_y > 744:
            self.float_y = 744 - 1

        
        self.rect.x = int(self.float_x)
        self.rect.y = int(self.float_y)
        
     
        
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        