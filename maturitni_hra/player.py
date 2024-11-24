import pygame
from getimg import get_image 
from bar import *
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,camera_group,animal_group):
        super().__init__() 
        self.x = 100
        self.y = 200
        self.spritesheet = pygame.image.load("image/entities/Player.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 0, 32, 31, 1) 
        self.speed = 1
        self.index = 0
        self.rect = self.image.get_rect(center = pos)
        self.camera_group = camera_group
        self.animal_group = animal_group
        self.wood = 5
        self.fire = False
        self.can_kill = False
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
    def fire_on(self):
        self.fire = True
        self.wood = self.wood - 5
    def update(self):
        dx = 0
        dy = 0
        
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
        elif key[pygame.K_k]:
            self.animation2(6)
            self.can_kill = True
        elif key[pygame.K_b] and self.wood >= 5:
            self.fire_on()
            #potřebuji aby se ubíralo pouze 5 dreva a ne vsechno 
            # musim vyřešit jak se bude přidavat drevo buď když hráč ujde nějakou vzdálenost nebo když bude držet klávesu e tak bude animace sekání do dřeva a bude se přidávat
            
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
        
       
        
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        