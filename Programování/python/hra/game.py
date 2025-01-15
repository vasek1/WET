from typing import Any
import pygame
from sys import exit
from settings import *
from utility import get_image
from player import Player
from monster import Monster
from world import World

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))



font = pygame.font.Font(None, 25)

game_over = False
elapsed_time = 0
mortal = True

monsters = pygame.sprite.Group()
player = pygame.sprite.GroupSingle()

desk_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
boost_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

sprite_groups = {
    "all_group": all_sprites,
    "player_group": player,
    "monsters_group": monsters,
    "coins_group": coin_group,
    "boost_group": boost_group,
    "desk_group": desk_group,

}
world = World("tiled/ucebna-final.tmx", screen, sprite_groups)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
  

    if game_over == False:
        
        screen.fill((255, 255, 255))
        #world.draw_background()

        text1 = font.render(f"Lives: {player.sprite.lives}", False, "#000000")
        text2 = font.render(f"Points: {player.sprite.score}", False, "#000000")
        screen.blit(text1, (1200, 10))
        screen.blit(text2, (1200, 30))

    
        
        player.update()

        monsters.update()
        all_sprites.draw(screen)
        
        player.sprite.mortal_time += clock.get_time()
        
        
       # if player.rect.colliderect(monster.rect):
       #     if not mortal:
       #      lives -= 1
       #      mortal = True
       #      elapsed_time = 0
             
        if player.sprite.lives <= 0:
            game_over = True
            
    else:
        screen.fill((0, 0, 0))
        over = font.render(f"Game Over", False, "#ff0000")
        screen.blit(over, (585,350))
        

 
    pygame.display.update()

   
    clock.tick(60)