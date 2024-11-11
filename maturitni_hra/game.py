import pygame
from random import randint
from sys import exit
import button
from player import Player
from settings import *
from map import Map
from camera import Camera
from bar import bar
from animal import Animal
from getimg import get_image 

pygame.init()
font1 = pygame.font.Font(None, 15)
font2 = pygame.font.Font(None, 90)
font3 = pygame.font.Font(None, 50)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

background = pygame.image.load("image/menu/start_background.png")
grave_image = pygame.image.load("image/gameover/grave.png")
tutorial_text = pygame.image.load("image/tutorial/tutorial.png")
under_bar= pygame.image.load("image/bars/under_bars.png")
health= pygame.image.load("image/bars/health.png")
water = pygame.image.load("image/bars/water.png")
food= pygame.image.load("image/bars/food.png")
tmp= pygame.image.load("image/bars/tmp.png")
start_image = pygame.image.load("image/menu/start_tlacitko.png")
exit_image= pygame.image.load("image/menu/exit_tlacitko.png")
play_again_image = pygame.image.load("image/gameover/play_again.png")
win_screen = pygame.image.load("image/gameover/win_screen.png")
tutorial_image = pygame.image.load("image/tutorial/skip_tlacitko.png")
see_image = pygame.image.load("image/sees/see1.png")
table_image = pygame.image.load("image/gameover/table_text.png")
level_data = ("image/map/mapa.tmx")

tutorial_button = button.Button(700,690, tutorial_image,width1=46,height1=22,scale= 5)
start_button = button.Button(450,320, start_image,width1=46,height1=22,scale=  7)
exit_button = button.Button(470,550, exit_image, width1=46,height1=22,scale= 6)

exit2_button = button.Button(500,570, exit_image, width1=46,height1=22,scale= 5)
play_again_button = button.Button(385,450,play_again_image,width1=92,height1=22,scale= 5)

exit3_button = button.Button(490,585, exit_image, width1=46,height1=22,scale= 5)
play_again2_button = button.Button(370,470,play_again_image,width1=92,height1=22,scale= 5)

see1 = pygame.Rect(238, 715, 70, 60)
see2 = pygame.Rect(898, 155, 100, 110)
see3 = pygame.Rect(870, 175, 160, 55)  

mapa = Map(screen,level_data)

health_bar = bar(1135,10,60,5,0,0,100,0)
water_bar = bar(1135,25,60,5,0,100,0,0)
food_bar = bar(1135,40,60,5,100,0,0,0)
temperature_bar = bar(1135,55,60,5,0,0,0,100)


animal_group = pygame.sprite.Group()
animal = Animal((800,750))
animal_group.add(animal)

camera_group = Camera(screen)
player = Player((600,750),camera_group,animal_group)
camera_group.add(player)

animal_spawn = pygame.time.get_ticks()
decrease_hp= pygame.time.get_ticks()
decrease_fd_wt= pygame.time.get_ticks()
increase_hp= pygame.time.get_ticks()
elapsed_time = 0
elapsed_time_day = 0
day = 0
start= True
Tutorial = False
Game_go = False
game_over = False
game_win = False
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
        game_over = False
        if tutorial_button.click(event):
            
            Game_go = True
            Tutorial = False  

    elif Game_go == True: 
        elapsed_time = pygame.time.get_ticks()
        elapsed_time_day = pygame.time.get_ticks()  / 600000 #600 000 nastavení dne na 10 minut

        offset = camera_group.center_target_camera(player)
        see1_offset = see1.move(-offset[0],-offset[1])
        see2_offset = see2.move(-offset[0],-offset[1])
        see3_offset = see3.move(-offset[0],-offset[1])    
        
        mapa.draw_background(offset)

        player.draw(screen)
        player.update()

        animal_group.update()
        for animal in animal_group:
            animal.draw(screen, offset)
            if not animal.live:
                animal.image = get_image(animal.spritesheet, 5, 5, 30, 30, 1)
                # vyřešit aby se přidalo 100 a pak se zase ubíralo i když je zvíře mrtvé
                food_bar.fd = 100
                if elapsed_time - decrease_fd_wt > 10000:
                    food_bar.fd -= 20
                if elapsed_time - animal_spawn >60000:
                    animal.image = get_image(animal.spritesheet, 0, 0, 30, 30, 1)            
                    animal.live = True
                    animal_spawn = elapsed_time

        screen.blit(see_image,see1_offset)
        screen.blit(see_image,see2_offset)
        screen.blit(see_image,see3_offset)

        screen.blit(under_bar,(1100,0))
        screen.blit(health,(1120,8))
        screen.blit(food,(1120,38))
        screen.blit(water,(1120,23))
        screen.blit(tmp,(1120,53))

        day_text = font1.render(f"Day: {day}", False, "#000000")
        wood_text = font1.render(f"Wood: {0}", False, "#000000")
        screen.blit(day_text, (1120, 67))
        screen.blit(wood_text, (1155, 67))

        health_bar.draw_Healthbar(screen)
        food_bar.draw_Foodbar(screen)
        water_bar.draw_Waterbar(screen)
        temperature_bar.draw_Temperaturebar(screen)
        
       

        
        
        
        if elapsed_time - decrease_fd_wt > 10000:
            water_bar.wt -= 20
            food_bar.fd -= 20
            temperature_bar.tp -= 5                  
            decrease_fd_wt = elapsed_time
        
        if food_bar.fd == 0 or water_bar.wt == 0:
          if health_bar.hp > 0 and elapsed_time - decrease_hp > 1000:
                health_bar.hp -= 5
                decrease_hp = elapsed_time

        
        if food_bar.fd > 75 and water_bar.wt > 75:
            if health_bar.hp < 100 and elapsed_time - increase_hp > 1000:
                 health_bar.hp += 10   
                 increase_hp = elapsed_time
        elif water_bar.wt > 75:
           if food_bar.fd > 0: 
            if health_bar.hp < 100 and elapsed_time - increase_hp > 1000:
                 health_bar.hp += 2    
                 increase_hp = elapsed_time
        elif food_bar.fd > 75:
           if water_bar.wt > 0:  
            if health_bar.hp < 100 and elapsed_time - increase_hp > 1000:
                 health_bar.hp += 2    
                 increase_hp = elapsed_time

        
        if player.rect.colliderect(see1_offset):
            water_bar.wt = 100
        elif player.rect.colliderect(see2_offset):
            water_bar.wt = 100
        elif player.rect.colliderect(see3_offset):
            water_bar.wt = 100
            
    
        if health_bar.hp <= 0:
         game_over =True
         Game_go = False
       
        if elapsed_time_day >=  10*day:
            day += 1
            elapsed_time_day = 0
        if day == 10:
            game_win = True   
            Game_go = False
            
    if game_over == True :
        text3 = font3.render(f"Days Survived: {day}", False,  "#000000")
        over = font2.render(f"YOU DIED", False, "#000000")
        screen.blit(background, (0, 0))
        screen.blit(grave_image, (370,190))
        screen.blit(text3, (478,380))
        screen.blit(over, (470,310))
        play_again_button.draw(screen)
        exit2_button.draw(screen) 
        if play_again_button.click(event):
            start = True
            game_over = False
            Tutorial = False
            Game_go = False
            health_bar.hp = 100
            water_bar.wt = 100
            food_bar.fd = 100
            temperature_bar.tp = 100
            day = 0
            elapsed_time_day = 0
            player.rect.x = 600
            player.rect.y = 750
        elif exit2_button.click(event):
            pygame.quit()
    if game_win == True:
        screen.blit(win_screen, (0, 0))
        screen.blit(table_image, (327,67))    
        play_again2_button.draw(screen)
        exit3_button.draw(screen)
        if play_again2_button.click(event):
            game_win = False
            start = True
            game_over = False
            Tutorial = False
            Game_go = False
            health_bar.hp = 100
            water_bar.wt = 100
            food_bar.fd = 100
            temperature_bar.tp = 100
            day = 0
            elapsed_time_day = 0
            player.rect.x = 600
            player.rect.y = 750
        elif exit3_button.click(event):
            pygame.quit()
    pygame.display.update() 
    clock.tick(60) 