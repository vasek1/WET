import pygame
from getimg import get_image 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.x = 100
        self.y = 200
        self.spritesheet = pygame.image.load("image/entities/Player.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 0, 31, 31, 10) 
        self.speed = 20
        self.index = 0
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        
       
    def animation(self, direction):
        frame_count = 6

        self.index += 0.2
        if self.index >= frame_count:
            self.index = 0

        self.image = get_image(self.spritesheet, int(self.index), direction, 31,31,10)

        
    def update(self):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= self.speed
            self.animation(2)
        if key[pygame.K_d]:
            dx += self.speed
            self.animation(4)
        if key[pygame.K_w]:
            dy -= self.speed
            self.animation(5)
        if key[pygame.K_s]:
            dy += self.speed
            self.animation(3)
        self.rect.x += dx
        self.rect.y += dy


    def draw(self, screen):
        screen.blit(self.image, self.rect)