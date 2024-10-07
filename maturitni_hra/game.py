import pygame
from sys import exit
import button
from player import Player

clock = pygame.time.Clock()
pygame.init()

background = pygame.image.load("image/menu/start_background.png")
tutorial_text = pygame.image.load("image/tutorial/tutorial.png")
screen_height = 800
screen_width =1200
screen = pygame.display.set_mode((screen_width, screen_height))


start_image = pygame.image.load("image/menu/start_tlacitko.png")
exit_image= pygame.image.load("image/menu/exit_tlacitko.png")
tutorial_image = pygame.image.load("image/tutorial/skip_tlacitko.png")
tutorial_button = button.Button(700,690, tutorial_image, 5)
start_button = button.Button(450,250, start_image, 7)
exit_button = button.Button(470,450, exit_image, 6)


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
            
        if exit_button.click(event):
                start = False
                exit()
        if Tutorial:
            screen.blit(tutorial_text,(0,0))
            tutorial_button.draw()
        if tutorial_button.click(event):
             Game_go = True
             tutorial = False
        if Game_go:
             screen.fill((34,139,34))
             player.update()
             player.draw(screen)
        pygame.display.update()
    clock.tick(60)