import pygame


pygame.init()

SCREEN_WIDTH = 800 #veci co jsou velkym by se neměli měnit
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
ctverec_surface = pygame.Surface((70,70))
ctverec_surface.fill((0,255,0))
ctverec = ctverec_surface.get_rect(topleft=(250, 300))

image = pygame.image.load("milos.jpg").convert_alpha()
img_rec = image.get_rect(topleft =(250,300))
zivot = 100

while running:
    for event in pygame.event.get():# projde všechny eventy ktere proběhly pokud se objeví event quit tak se vypne
        if event.type == pygame.QUIT: #pokud je quit tak se vypne
            running = False


    if ctverec.colliderect(img_rec) and zivot > 0:
        zivot -= 1
        print(zivot)
    elif zivot <= 0:
        print("Gameover")
        screen.fill((0,0,255))

    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        ctverec.y -= 5
    if key[pygame.K_s]:
        ctverec.y += 5
    if key[pygame.K_a]:
        ctverec.x -= 5   
    if key[pygame.K_d]:
        ctverec.x += 5


    if zivot > 0:
      screen.fill((0,0,0))#tuple()
      screen.blit(ctverec_surface, ctverec)
      screen.blit(image, (img_rec))

    pygame.display.update()
    clock.tick(60)  
pygame.quit()