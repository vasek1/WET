import pygame
from sys import exit
from screen import *
from player import Player
player = Player
pygame.init()
clock =pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255, 255, 255))

    player.draw(screen)

    pygame.display.update()
    clock.tick(60)






   
