import pygame
from sys import exit

pygame.init()


screen_height = 800
screen_width =1200
screen = pygame.display.set_mode((screen_width, screen_height))





while True:

    for event in pygame.event.get():
     
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    
    pygame.display.update()