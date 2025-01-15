import pygame

class bar():
    def __init__(self,x,y,w,h,max_fd,max_wt,max_hp,max_tp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.fd = max_fd
        self.max_fd = max_fd
        self.wt = max_wt
        self.max_wt = max_wt
        self.hp = max_hp
        self.max_hp = max_hp
        self.tp = max_tp
        self.max_tp = max_tp
    def draw_Healthbar (self,surface):
        ratio = self.hp/ self.max_hp
        red =(139, 0, 0)
        pygame.draw.rect(surface,red, (self.x,self.y,self.w,self.h,))
        pygame.draw.rect(surface,"green", (self.x,self.y,self.w*ratio,self.h,))
    def draw_Waterbar (self,surface):
        ratio = self.wt/ self.max_wt
        blue =	(0, 191, 255)
        red =(139, 0, 0)
        pygame.draw.rect(surface,red, (self.x,self.y,self.w,self.h,))
        pygame.draw.rect(surface,blue, (self.x,self.y,self.w*ratio,self.h,))
    def draw_Foodbar (self,surface):
        ratio = self.fd/ self.max_fd
        brown = (181, 101, 29)
        red =(139, 0, 0)
        pygame.draw.rect(surface,red, (self.x,self.y,self.w,self.h,))
        pygame.draw.rect(surface,brown, (self.x,self.y,self.w*ratio,self.h,))
    def draw_Temperaturebar (self,surface):
        ratio = self.tp/ self.max_tp
        blue = (106, 90, 205)
        red =(220, 60, 50)
        pygame.draw.rect(surface,blue, (self.x,self.y,self.w,self.h,))
        pygame.draw.rect(surface,red, (self.x,self.y,self.w*ratio,self.h,))