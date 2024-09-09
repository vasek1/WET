import pygame
from sys import exit
import button


pygame.init()


screen_height = 800
screen_width =1200
screen = pygame.display.set_mode((screen_width, screen_height))

start_img = pygame.image.load("image/menu/start_tlacitko.png")
exit_img= pygame.image.load("image/menu/exit_tlacitko.png")
start_button = button.Button(400,300, start_img)
exit_button = button.Button(100,600, exit_img)

while True:

    for event in pygame.event.get():
     
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.fill((0,0,0))
        start_button.draw()
        exit_button.draw()



    
        pygame.display.update()