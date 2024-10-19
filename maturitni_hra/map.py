import pygame
from pytmx.util_pygame import load_pygame

class Map:
     def __init__(self,screen, level_data):
          self.data = load_pygame(level_data)
          self.screen = screen
          self.background = pygame.Surface((self.data.width * self.data.tilewidth, self.data.height * self.data.tileheight))
          self.pozadi_layer = self.data.get_layer_by_name('pozadi')
          self.jezera_layer = self.data.get_layer_by_name('jezera')
          self.priroda_layer = self.data.get_layer_by_name('priroda')
          self.zvirata_layer = self.data.get_layer_by_name('zvirata_plocha')
     def draw_background(self):
        
        for x, y, image in self.pozadi_layer.tiles():
            self.background.blit(image, (x * self.data.tilewidth, y * self.data.tileheight))
        self.screen.blit(self.background, (0,0))
        for x, y, image in self.jezera_layer.tiles():
                self.background.blit(image, (x * self.data.tilewidth, y * self.data.tileheight))
        self.screen.blit(self.background, (0, 0))
        for x, y, image in self.priroda_layer.tiles():
                self.background.blit(image, (x * self.data.tilewidth, y * self.data.tileheight))
        self.screen.blit(self.background, (0, 0))
        for x, y, image in self.zvirata_layer.tiles():
                self.background.blit(image, (x * self.data.tilewidth, y * self.data.tileheight))
        self.screen.blit(self.background, (0, 0))