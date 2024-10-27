import pygame
from random import randint
from sys import exit
import button
from player import Player
from settings import *
from map import Map
from camera import Camera
from bar import bar
import pytmx

clock = pygame.time.Clock()
pygame.init()
font2 = pygame.font.Font(None, 100)
font3 = pygame.font.Font(None, 50)
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("image/menu/start_background.png")
tutorial_text = pygame.image.load("image/tutorial/tutorial.png")
under_bar= pygame.image.load("image/bars/under_bars.png")
health= pygame.image.load("image/bars/health.png")
water = pygame.image.load("image/bars/water.png")
food= pygame.image.load("image/bars/food.png")
start_image = pygame.image.load("image/menu/start_tlacitko.png")
exit_image= pygame.image.load("image/menu/exit_tlacitko.png")
play_again_image = pygame.image.load("image/gameover/play_again.png")
tutorial_image = pygame.image.load("image/tutorial/skip_tlacitko.png")
level_data = ("image/map/mapa.tmx")

tutorial_button = button.Button(700,690, tutorial_image,width1=46,height1=22,scale= 5)
start_button = button.Button(450,250, start_image,width1=46,height1=22,scale=  7)
exit_button = button.Button(470,450, exit_image, width1=46,height1=22,scale= 6)
play_again_button = button.Button(400,600,play_again_image,width1=92,height1=22,scale= 5)

mapa = Map(screen,level_data)
health_bar = bar(1135,10,60,5,0,0,100,)
water_bar = bar(1135,25,60,5,0,100,0)
food_bar = bar(1135,40,60,5,100,0,0)

player = pygame.sprite.GroupSingle()
player.add(Player()) 

start= True
Tutorial = False
Game_go = False
game_over = False

while True:

    for event in pygame.event.get():
     
        if event.type == pygame.QUIT:
            pygame.quit()    
        screen.blit(background, (0, 0))
    if start == True:  
        start_button.draw(screen)
        exit_button.draw(screen)
        
        if start_button.click(event):
            Tutorial = True
            start = False  
        
        if exit_button.click(event):
            pygame.quit()
            

    elif Tutorial == True:  
        screen.blit(tutorial_text, (0, 0))
        tutorial_button.draw(screen)

        if tutorial_button.click(event):
            Game_go = True
            Tutorial = False  

    elif Game_go == True: 
        mapa.draw_background()
        player.update()
        player.draw(screen)
        #lišta v rohu
        screen.blit(under_bar,(1100,0))
        health_bar.draw_Healthbar(screen)
        screen.blit(health,(1120,8))
        food_bar.draw_Foodbar(screen)
        screen.blit(food,(1120,38))
        water_bar.draw_Waterbar(screen)
        screen.blit(water,(1120,23))
        health_bar.hp = 10
        food_bar.fd = 30
        water_bar.wt = 50
            # camera.update()
             #camera.custom_draw(screen)
        if health_bar.hp <= 0:
         game_over =True
         Game_go = False
    if game_over == True :
        screen.blit(background, (0, 0))
        text3 = font3.render(f"Days Survived: {3}", False,  "#ff0000")
        over = font2.render(f"YOU LOSE", False, "#ff0000")
        screen.blit(text3, (485,400))
        screen.blit(over, (450,310))
        play_again_button.draw(screen)    
    if play_again_button.click(event):
        start = True
        game_over = False
        start_button.draw(screen)
        exit_button.draw(screen)

    pygame.display.update() 
    clock.tick(60) 