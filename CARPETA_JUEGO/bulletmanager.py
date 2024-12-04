import pygame
from auxiliar import *
from bullet import Bullet


class BulletManager():
    def __init__(self,cantidad_balas_player,cantidad_balas_enemigo):
        self.balas_player = [Bullet() for _ in range(cantidad_balas_player)]
        self.balas_enemy =  [Bullet() for _ in range(cantidad_balas_enemigo)]
        self.balas_disparadas = []
        self.cantidad_balas = cantidad_balas_player
        self.last_shot_time = 0  # Tiempo del último disparo

        

    def create_bullet(self,cantidad):
           return [Bullet() for _ in range(cantidad)] 

    def shoot(self, x_player, y_player, direction, controllable):
        current_time = pygame.time.get_ticks()  # Obtén el tiempo actual

        if controllable:  # Si el disparo es controlado por el jugador
            if self.balas_player and (current_time - self.last_shot_time >= 300):  # Cooldown de 300 ms
                self.last_shot_time = current_time
                bala_actual = self.balas_player.pop(0)
                bala_actual.player_bullet = True
                bala_actual.bullet_rect.x = x_player
                bala_actual.bullet_rect.y = y_player
                bala_actual.shoot_direction = direction
                bala_actual.is_shooting = True
                self.balas_disparadas.append(bala_actual)
                print("Bala disparada por el jugador")
            else:
                print("Esperando cooldown o sin balas disponibles")
        else:  # Si el disparo es de un enemigo
            if self.balas_enemy:
                bala_actual_enemigo = self.balas_enemy.pop(0)
                bala_actual_enemigo.bullet_rect.x = x_player
                bala_actual_enemigo.bullet_rect.y = y_player
                bala_actual_enemigo.shoot_direction = direction
                bala_actual_enemigo.is_shooting = True
                self.balas_disparadas.append(bala_actual_enemigo)
                print("Bala disparada por un enemigo")

           
        
    def reload(self):
             self.balas_player.clear()
             self.balas_player = self.create_bullet(self.cantidad_balas) 
             


