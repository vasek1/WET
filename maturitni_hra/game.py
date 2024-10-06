import pygame
from sys import exit
import button

clock = pygame.time.Clock()
pygame.init()

background = pygame.image.load("image/menu/background_menu.png")
tutorial_text = pygame.image.load("image/tutorial/tutorial_s_napisem.png")
screen_height = 800
screen_width =1200
screen = pygame.display.set_mode((screen_width, screen_height))


start_image = pygame.image.load("image/menu/start_tlacitko.png")
exit_image= pygame.image.load("image/menu/exit_tlacitko.png")
tutorial_image = pygame.image.load("image/tutorial/skip_tlacitko.png")
tutorial_button = button.Button(700,690, tutorial_image, 5)
start_button = button.Button(416,200, start_image, 8)
exit_button = button.Button(416,500, exit_image, 8)
start= True
Tutorial = False
Game_go = False
while True:

    for event in pygame.event.get():
     
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
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
        if Game_go:
             screen.blit(background,(0,0))
        pygame.display.update()