import pygame
from utility import get_image
from settings import *
import time



class Player(pygame.sprite.Sprite):
    def __init__(self, position, sprite_groups):
        super().__init__()
        self.position = position
        self.index = 0
        self.spritesheet = pygame.image.load("assets/player/man_brownhair_run.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 0, 15, 16, 3)
        self.rect = self.image.get_rect(topleft=(self.position))
        self.lives = 2
        self.boosts = 0
        self.eat_monster = False
        self.score = 0
        self.mortal = False
        self.mortal_time =0
        self.width = 15
        self.height =16
        self.speed = 8
        self.scale = 3
        self.text_time = None
        self.font =pygame.font.Font(None,400)
        
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


        if self.mortal_time > 1000:
            self.mortal = False
            self.speed = 8
        
        if self.boosts == 5:
            self.mortal = True

            if self.text_time is None:
                self.text_time = time.time()
            if time.time() - self.text_time <= 2:
                    snez = self.font.render("KILL ALL", False, "#ff0000")
                    screen.blit(snez, (15, 50))
                    snez2 = self.font.render("ENEMIES", False, "#ff0000")
                    screen.blit(snez2, (20, 400))   

        for monster in pygame.sprite.spritecollide(self, self.monsters_group, False): 
            if self.eat_monster:
                monster.kill()
                self.score += 20
                self.scale = self.scale + 0.8

            if not self.mortal:
                 self.lives -= 1
                 self.mortal = True
                 self.scale = self.scale - 0.6
                 self.mortal_time= 0
                 self.speed = 10

        if pygame.sprite.spritecollide(self, self.coins_group, True):
            self.score += 1
        if pygame.sprite.spritecollide(self, self.boost_group, True):
            self.lives += 1
            self.scale = self.scale + 0.6
            self.boosts +=1
            self.speed -=1
            if self.boosts >= 5:
                self.eat_monster = True


    def animation(self, direction):
     frame_count = 4
     self.index += 0.1
     if self.index >= frame_count:
        self.index = 0
            
     self.image = get_image(self.spritesheet,int(self.index),direction,15, 16,self.scale)

    
    def draw(self,screen):
         screen.blit(self.image, self.rect)

  
