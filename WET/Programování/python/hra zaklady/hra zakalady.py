import pygame
from sys import exit

#spustíme hru
pygame.init()

clock =pygame.time.Clock()

screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))
#(x, y začínající pozice, šířka, výška)
player = pygame.Rect((100, 200, 50, 50))
while True:
    #kontroluje události
    for event in pygame.event.get():
        #aby se hra vypla
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        player.move_ip(-10, 0)
    if key[pygame.K_RIGHT] == True:     # kdyz  bude elif muzu se hybat sikmo kdyz if tak ne
        player.move_ip(10, 0)
    if key[pygame.K_UP] == True:
        player.move_ip(0, -10)
    if key[pygame.K_DOWN] == True:
        player.move_ip(0, 10)
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.display.update()
    #obnovovací frekvence 60 snimku za sekundu
    clock.tick(60)
