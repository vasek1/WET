import pygame
from random import randint
from sys import exit
import button
from player import Player
from settings import *
from map import Map

import pytmx

clock = pygame.time.Clock()
pygame.init()

background = pygame.image.load("image/menu/start_background.png")
tutorial_text = pygame.image.load("image/tutorial/tutorial.png")

screen = pygame.display.set_mode((screen_width, screen_height))


start_image = pygame.image.load("image/menu/start_tlacitko.png")
exit_image= pygame.image.load("image/menu/exit_tlacitko.png")
tutorial_image = pygame.image.load("image/tutorial/skip_tlacitko.png")
tutorial_button = button.Button(700,690, tutorial_image, 5)
start_button = button.Button(450,250, start_image, 7)
exit_button = button.Button(470,450, exit_image, 6)

level_data = "image/map/mapa.tmx"
mapa = Map(screen,level_data)

player = pygame.sprite.GroupSingle()
player.add(Player()) 

start= True
Tutorial = False
Game_go = False
while True:

    for event in pygame.event.get():
     
        if event.type == pygame.QUIT:
            pygame.quit()
            
       
        screen.blit(background,(0,0))
        start_button.draw()
        exit_button.draw()
        
    
        if start_button.click(event):
            Tutorial = True  
        if not Tutorial:
            if exit_button.click(event):
                exit()
               
        if Tutorial:
            screen.blit(tutorial_text,(0,0))
            tutorial_button.draw()
        if tutorial_button.click(event):
             Game_go = True
             Tutorial = False
        if Game_go:
             mapa.draw_background()
             player.update()
             player.draw(screen)
             
    pygame.display.update()
    clock.tick(60)