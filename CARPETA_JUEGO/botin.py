import pygame

from auxiliar import *




class Botin:
    
    def __init__(self,x,y,w,h,type=0):
        self.image = Auxiliar.getSurfaceFromSpriteSheet("resources/Bullet/fire.png",1,1)
        self.frame = 0
        self.image = self.image[self.frame]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect() 
        self.rect.x = x 
        self.rect.y = y
        self.rect_botin_collition = self.rect
        

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,GREEN,self.rect_botin_collition)

        screen.blit(self.image,self.rect)

        