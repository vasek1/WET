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


font1 = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 100)
font3 = pygame.font.Font(None, 50)

obrazek= pygame.image.load("vyhra.png")
vyherni_obrazek = pygame.transform.scale(obrazek, (screen_width, screen_height))

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
  #pridat hudbu do pozadí a zvukový efekty
    if game_over == False:
        
            
        screen.fill((255, 255, 255))
    

        text1 = font1.render(f"Lives: {player.sprite.lives}", False, "#000000")
        text2 = font1.render(f"Points: {player.sprite.score}", False, "#000000")
        screen.blit(text1, (1200, 10))
        screen.blit(text2, (1200, 30))
        
        
        
        player.update()
        
        monsters.update()
        all_sprites.draw(screen)
        
        player.sprite.mortal_time += clock.get_time()

        
        if player.sprite.lives <= 0:
            game_over = True
        if player.sprite.score >= 119:
            game_over = True

    elif player.sprite.score == 119:
        game_over = True
        screen.fill((0, 0, 0))
        win = font2.render(f"YOU WIN", False, "#ff0000")
        text3 = font3.render(f"Points: {player.sprite.score}", False,  "#ff0000")
        
        screen.blit(vyherni_obrazek, (0,0))
        screen.blit(text3, (565,400))
        screen.blit(win, (475,310))
    else:
        screen.fill((0, 0, 0))
        text3 = font3.render(f"Points: {player.sprite.score}", False,  "#ff0000")
        over = font2.render(f"YOU LOSE", False, "#ff0000")

        screen.blit(text3, (550,400))
        screen.blit(over, (450,310))
        
    pygame.display.update()

   
    clock.tick(60)