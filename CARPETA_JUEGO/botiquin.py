import pygame
from auxiliar import *




class Botiquin:
    
    def __init__(self,x,y,w,h,type=0):
        self.image = Auxiliar.getSurfaceFromSpriteSheet("images/assets/bag_elemental_pouch/bag_elemental_pouch__x1_1_png_1354831495.png",1,1)[type]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = self.rect
        

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,GREEN,self.rect)

        screen.blit(self.image,self.rect)

        