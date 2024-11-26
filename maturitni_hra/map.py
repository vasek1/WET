import pygame
from pytmx.util_pygame import load_pygame

class Map:
     def __init__(self,screen, level_data):
          self.data = load_pygame(level_data)
          self.screen = screen
          
          self.background = pygame.Surface((self.data.width * self.data.tilewidth, self.data.height * self.data.tileheight))
          self.tree = self.data.get_layer_by_name('tree')
          self.pozadi_layer = self.data.get_layer_by_name('pozadi')
          self.jezera_layer = self.data.get_layer_by_name('jezera')
          self.more_layer = self.data.get_layer_by_name('more')
          self.priroda_layer = self.data.get_layer_by_name('priroda')
          self.stromy_layer = self.data.get_layer_by_name('stromy')
          self.zvirata_layer = self.data.get_layer_by_name('zvirata_plocha')
          self.layers = [self.pozadi_layer, self.jezera_layer, self.priroda_layer, self.zvirata_layer,self.more_layer]
          #přidat stromy jako objekty nebo jako vrstvu  musíme poradit proč mi to stromy vykresluje výš kdyz je dávám jako vrstvu a ne tam kde jsem je namaloval
     def draw_background(self, offset):
        for layer in self.layers:
            for x, y, image in layer.tiles():
                self.background.blit(
                    image,
                    (
                        (x * self.data.tilewidth) - offset[0] ,
                        (y * self.data.tileheight) - offset[1] ,
                    ),
                )
        self.screen.blit(self.background, (0, 0))
        
     def draw_trees(self,offset):
        for x, y, image in self.stromy_layer.tiles():
         self.screen.blit(
            image,
            (
                (x * self.data.tilewidth) - offset[0],
                (y * self.data.tileheight) - offset[1],
            ),
        )