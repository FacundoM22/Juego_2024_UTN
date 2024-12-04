import pygame
from auxiliar import *
from bulletmanager import *


class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,healt, energia, bullets,live) -> None:
         self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\pixel\Heroes\Rogue\Run\Run-Sheet.png", 6, 1)
         self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\pixel\Heroes\Rogue\Run\Run-Sheet_L.png", 6, 1)
         self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\pixel\Heroes\Rogue\Idle\Idle-Sheet.png",4,1)
         self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\pixel\Heroes\Rogue\Idle\Idle-Sheet_L.png",4,1)
         self.jump_r =  Auxiliar.getSurfaceFromSpriteSheet(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\pixel\Heroes\Rogue\Run\Run-Sheet.png", 6, 1)
         self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\pixel\Heroes\Rogue\Run\Run-Sheet_L.png", 6, 1)
         self.frame = 0
         self.lived = 1
         self.live = live
         self.energia = energia
         self.bullets = bullets
         self.x_spot = x
         self.y_spot = y
         self.lives = 1
         self.health = healt
         self.move_x = 0
         self.move_y = 0
         self.speed_walk = speed_walk #Obtenido por parametro
         self.speed_run = speed_run
         self.gravity = gravity
         self.jump_power = jump_power
         self.animation = self.stay_l #Seteamos la animacion del personaje.
         self.direction = DIRECTION_L
         self.image = self.animation[self.frame] #Seleccionamos el frame de la lista animation.
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         self.is_jump = False
         self.tiempo_transcurrido_animation = 0
         self.tiempo_transcurrido_enemy_move = 0
         self.frame_rate_ms = frame_rate_ms
         self.tiempo_transcurrido_move = 0
         self.move_rate_ms = move_rate_ms
         self.y_start_jump = 0
         self.jump_height = jump_height
         self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 3, GROUND_RECT_H)  # Analizar a fondo que es importante
         self.rect_character_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + 25, self.rect.w/4, self.rect.h / 2)

    def walk(self,direction):
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.frame = 0
            self.direction = direction
            if(direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l

    def jump(self,on_off = True):
     if(self.energia <= 0):
         pass
     else:
        if(on_off and self.is_jump == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_r
                self.energia = self.energia - 20 # Energia
            else:
                self.move_x = -self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_l
                self.energia = self.energia - 20 # Energia
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()


    def stay(self):
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def is_on_platform(self,lista_plataformas):
        retorno = False
        if(self.rect.y >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)): #Comprobamos si existe una colision entre el rectangulo del personaje y el rectangulo de la plataforma
                    retorno = True
                    break   
        return retorno
    
    
    def is_shooted(self, lista_balas):
            for bala in lista_balas:
                if self.rect_character_collition.colliderect(bala.rect_bullet_collition) and bala.player_bullet == True:
                            self.health -= 50
                            print("Colisiono bala: {0}".format(bala.rect_bullet_collition))
                            print(self.health)
                            lista_balas.pop(lista_balas.index(bala))   


    def state(self, lista_enemigos):
        for enemigo in lista_enemigos:
            # Verifica si el objeto tiene el atributo 'health'
            if hasattr(enemigo, 'health') and enemigo.health <= 0:
                enemigo.lived = 0
                lista_enemigos.pop(lista_enemigos.index(enemigo))


    def do_movement(self,delta_ms,lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if(abs(self.y_start_jump)- abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0

            self.tiempo_transcurrido_move = 0
            self.add_x(self.move_x)
            self.add_y(self.move_y)


            if(self.is_on_platform(lista_plataformas) == False):
                 self.add_y(self.gravity)
            elif(self.is_jump): #Â SACAR
                self.jump(False)

 

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def add_x(self,delta_x):
        self.rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.rect_character_collition.x += delta_x

    def add_y(self,delta_y):
        self.rect.y += delta_y  
        self.rect_ground_collition.y += delta_y
        self.rect_character_collition.y += delta_y


    def update(self,delta_ms,lista_plataformas,lista_players,lista_balas):
        self.do_movement(delta_ms,lista_plataformas)
        self.do_animation(delta_ms)
        self.state(lista_players)
      #  self.is_shooted(lista_balas)
        
    
    def draw(self,screen,lista_enemigo):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
            pygame.draw.rect(screen,GREEN,self.rect_character_collition)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)


    def events(self, keys):
    # Movimiento a la izquierda
        if keys[pygame.K_LEFT]:  
            self.walk(DIRECTION_L)
        # Movimiento a la derecha
        elif keys[pygame.K_RIGHT]:  
            self.walk(DIRECTION_R)
        # Salto
        elif keys[pygame.K_UP]:  
            self.jump(True)
        else:
            # Detener movimiento cuando no se presiona nada relevante
            self.stay()


      


                
        
            
        


