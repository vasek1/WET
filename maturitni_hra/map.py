import pygame
from pytmx.util_pygame import load_pygame

class Map:
     def __init__(self,screen, level_data):
          self.data = load_pygame(level_data)
          self.screen = screen
          self.background = pygame.Surface((self.data.width * self.data.tilewidth, self.data.height * self.data.tileheight))
          self.pozadi_layer = self.data.get_layer_by_name('pozadi')
          self.jezera_layer = self.data.get_layer_by_name('jezera')
          self.more_layer = self.data.get_layer_by_name('more')
          self.priroda_layer = self.data.get_layer_by_name('priroda')
          self.zvirata_layer = self.data.get_layer_by_name('zvirata_plocha')
          self.layers = [self.pozadi_layer, self.jezera_layer, self.priroda_layer, self.zvirata_layer,self.more_layer]
     def draw_background(self, offset):
        for layer in self.layers:
            for x, y, image in layer.tiles():
                self.background.blit(
                    image,
                    (
                        (x * self.data.tilewidth) - offset[0],
                        (y * self.data.tileheight) - offset[1],
                    ),
                )
        self.screen.blit(self.background, (0, 0))
          