import pygame
from pytmx.util_pygame import load_pygame
from tree import Tree

class Map:
     def __init__(self,screen, level_data,tree_group):
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
          self.tree_group = tree_group
          self.layers = [self.pozadi_layer, self.jezera_layer, self.priroda_layer, self.zvirata_layer,self.more_layer]
          
          #přidat stromy jako objekty nebo jako vrstvu  musíme poradit proč mi to stromy vykresluje výš kdyz je dávám jako vrstvu a ne tam kde jsem je namaloval
          self.create_tree()
     def draw_background(self,internal_surf, offset):
        for layer in self.layers:
            for x, y, image in layer.tiles():
                internal_surf.blit(
                    image,
                    (
                        (x * self.data.tilewidth) - offset[0] ,
                        (y * self.data.tileheight) - offset[1] ,
                    ),
                )
        #self.camera.internal_surf.blit(self.background, (0, 0))
        
     def draw_trees(self,internal_surf,offset):
        for x, y, image in self.stromy_layer.tiles():
            internal_surf.blit(
            image,
            (
                (x * self.data.tilewidth) - offset[0],
                (y * self.data.tileheight) - offset[1],
            ),
        )

     def create_tree(self):
        for tree in self.tree:
            new_tree = Tree(tree.image, tree.width, tree.height, (tree.x, tree.y))
            self.tree_group.add(new_tree)
        

     #def create_tree(self, offset):
     #   for tree in self.tree:
      #      new_tree = Tree(tree.image, tree.width, tree.height, (tree.x, tree.y))
       #     self.tree_group.add(new_tree)

