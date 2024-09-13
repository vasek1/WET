import pygame
from sys import exit
import button

clock = pygame.time.Clock()
pygame.init()

background = pygame.image.load("image/menu/background_menu.png")
tutorial_text = pygame.image.load("image/tutorial_s_napisem.png")
screen_height = 800
screen_width =1200
screen = pygame.display.set_mode((screen_width, screen_height))


start_image = pygame.image.load("image/menu/start_tlacitko.png")
exit_image= pygame.image.load("image/menu/exit_tlacitko.png")
start_button = button.Button(416,200, start_image, 8)
exit_button = button.Button(416,500, exit_image, 8)
bezi = True
Tutorial = False
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
                bezi = False
                exit()
        if Tutorial:
            screen.blit(tutorial_text,(0,0))

    
        pygame.display.update()