import pygame
from getimg import get_image 

class Animal(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__() 
        self.x = 900
        self.y = 600
        self.postion = position
        self.spritesheet = pygame.image.load("image/entities/Chicken.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 0, 30, 30, 1) 
        self.index = 0
        self.rect = self.image.get_rect(topleft=(position))
        self.direction = "Left"
        self.speed = 1
        self.rect.y = 900
        self.live = True
    def animation(self, direction):
        frame_count = 2

        self.index += 0.1

        if self.index >= frame_count:
            self.index = 0

        self.image = get_image(self.spritesheet, int(self.index), direction, 30,30,1)

    def dead(self):
        self.live = False
        
    def update(self):
            if self.live:
                if self.rect.x <= 840:
                    self.direction = "Right"
                    self.animation(0)
                elif self.rect.x >= 900:
                    self.direction = "Left"
                    self.animation(1)
                if self.direction == "Left":
                    self.rect.x -= self.speed
                    self.animation(1)
                elif self.direction == "Right":
                    self.rect.x += self.speed
                    self.animation(0)
            
    def  draw(self,screen,camera_offset):
        screen.blit(self.image, (self.rect.x - camera_offset[0], self.rect.y - camera_offset[1]))
