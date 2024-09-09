import pygame
from utility import get_image
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, sprite_groups):
        super().__init__()
        self.position = position
        self.index = 0
        self.spritesheet = pygame.image.load("assets/player/man_brownhair_run.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 0, 15, 16, 3)
        self.rect = self.image.get_rect(topleft=(self.position))
        self.lives = 3
        self.score = 0
        self.mortal = False
        self.mortal_time =0
        self.width = 15
        self.height =16
        self.speed = 10
        self.scale = 3
        
        for key,group in sprite_groups.items():
            setattr(self,key, group)
            
    def update(self): 
        dx = 0
        dy = 0
     
        

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]: 
            dx -= self.speed
            self.animation(2)
        elif key[pygame.K_RIGHT]:
            dx += self.speed
            self.animation(3)
        elif key[pygame.K_UP]:
            dy-= self.speed
            self.animation(1)
        elif key[pygame.K_DOWN]:
            dy+= self.speed
            self.animation(0)
        
        self.rect.x += dx
        self.rect.y += dy
        for desks in pygame.sprite.spritecollide(self,self.desk_group, False):
            if dx > 0 :
                self.rect.right = desks.rect.left
            if dx < 0 :
                self.rect.left = desks.rect.right
            if dy > 0 :
                self.rect.bottom = desks.rect.top
            if dy < 0 :
                self.rect.top = desks.rect.bottom


        if self.rect.x < 0:
            self.rect.x = screen_width -10
        elif self.rect.x> screen_width:
            self.rect.x = 10
        if self.rect.y < 0:
            self.rect.y = screen_height-10
        elif self.rect.y> screen_height:
            self.rect.y = 10


        if self.mortal_time > 2000:
            self.mortal = False
            self.speed = 10
    

        if pygame.sprite.spritecollide(self, self.monsters_group, False):     
            if not self.mortal:
                 self.lives -= 1
                 self.mortal = True
                 self.mortal_time= 0
                 self.speed = 30

        if pygame.sprite.spritecollide(self, self.coins_group, True):
            self.score += 1
        if pygame.sprite.spritecollide(self, self.boost_group, True):
            self.lives += 1
            self.scale = self.scale + 1
            
   
      
        
        

    def animation(self, direction):
     frame_count = 4
     self.index += 0.1
     if self.index >= frame_count:
        self.index = 0
            
     self.image = get_image(self.spritesheet,int(self.index),direction,15, 16,self.scaley)

    
    def draw(self,screen):
         screen.blit(self.image, self.rect)
