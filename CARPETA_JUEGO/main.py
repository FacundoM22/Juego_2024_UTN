import pygame
import sys
from tkinter import *
from bulletmanager import *
from player import Player
from enemigo import Enemigo
#from plataforma import Platform
from auxiliar import *
from button import *
from botiquin import Botiquin
#from trampa import Trampa
from fuctions import *
#from portal import Portal
from botin import Botin
#from SQLITE import *
lista_plataformas = []
username = ""
music = True

clock = pygame.time.Clock()

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


fuente = pygame.font.SysFont("Cambria",31)

Background = pygame.image.load(r"C:\Users\Facundo\Desktop\JUEGO UTN 2024\Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\background\vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310_640\vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310.jpg")


def mostar_ranking():
    while True:
        screen.blit(Background,(0,0))
        

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = fuente.render("RANKING:", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=((ANCHO_VENTANA/2), 100))

        QUIT_BUTTON = Button(image=pygame.image.load(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\STOP.jpg"), pos=((ANCHO_VENTANA/2), 550), 
                            text_input="SALIR", font=fuente, base_color="#d7fcd4", hovering_color="Black")

        screen.blit(MENU_TEXT, MENU_RECT)


        for button in [QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
          
        pygame.display.update()


def seleccionar_nivel():
    while True:

            screen.blit(Background,(0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = fuente.render("SELECCIONA EL NIVEL:", True, "Black")
            MENU_RECT = MENU_TEXT.get_rect(center=((ANCHO_VENTANA/2), 100))

            LEVEL1_BUTTON = Button(image=pygame.image.load(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\START.jpg"), pos=((ANCHO_VENTANA/2), 250), 
                    text_input="NIVEL 1", font=fuente, base_color="#d7fcd4", hovering_color="Black")
            LEVEL2_BUTTON = Button(image=pygame.image.load(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\PAUSE.jpg"), pos=((ANCHO_VENTANA/2), 400), 
                    text_input="NIVEL 2", font=fuente, base_color="#d7fcd4", hovering_color="Black")
            LEVEL3_BUTTON = Button(image=pygame.image.load(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\STOP.jpg"), pos=((ANCHO_VENTANA/2), 550), 
                    text_input="NIVEL 3", font=fuente, base_color="#d7fcd4", hovering_color="Black")

            screen.blit(MENU_TEXT, MENU_RECT)


            for button in [LEVEL1_BUTTON, LEVEL2_BUTTON, LEVEL3_BUTTON]:
              button.changeColor(MENU_MOUSE_POS)
              button.update(screen)

            for event in pygame.event.get():
             if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
             if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL1_BUTTON.checkForInput(MENU_MOUSE_POS):
                  play(pausa,1)
                if LEVEL2_BUTTON.checkForInput(MENU_MOUSE_POS):
                 play(pausa,2)
                if LEVEL3_BUTTON.checkForInput(MENU_MOUSE_POS):
                 play(pausa,3)

            pygame.display.update()

        


def main_menu():
    global username
    global music
    text = "MUSIC ON"
    input_rect = pygame.Rect((ANCHO_VENTANA/2.1),700,140,32)
    color = pygame.Color('Black')
    unlocked = False
    while True:
        screen.blit(Background,(0,0))
        

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = fuente.render("MENU PRINCIPAL", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=((ANCHO_VENTANA/2), 100))

        PLAY_BUTTON = Button(image=pygame.image.load(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\START.jpg"), pos=((ANCHO_VENTANA/2), 250), 
                            text_input="JUGAR", font=fuente, base_color="#d7fcd4", hovering_color="Black")
        OPTIONS_BUTTON = Button(image=pygame.image.load(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\START.jpg"), pos=((ANCHO_VENTANA/2), 400), 
                            text_input= text , font=fuente, base_color="#d7fcd4", hovering_color="Black")
        QUIT_BUTTON = Button(image=pygame.image.load(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\START.jpg"), pos=((ANCHO_VENTANA/2), 550), 
                            text_input="SALIR", font=fuente, base_color="#d7fcd4", hovering_color="Black")

        screen.blit(MENU_TEXT, MENU_RECT)


        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                   seleccionar_nivel()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if music == True:
                        music = False
                        text =  OPTIONS_BUTTON.text_input  = "MUSIC OFF"
                    else:
                        music = True
                        text = OPTIONS_BUTTON.text_input = "MUSIC ON"
                       
                        
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    unlocked = True
                    
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    if unlocked == False:
                        username += event.unicode
              
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
              button.changeColor(MENU_MOUSE_POS)
              button.update(screen)

        pygame.draw.rect(screen,color,input_rect,2)
        text_surface = fuente.render(username,True,(255,255,255))
        input_rect.w = max(100,text_surface.get_width()+10)


        texto_username = fuente.render("USERNAME", True, "Black")


        screen.blit(texto_username,(input_rect.x - 20,input_rect.y - 60))
        screen.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
        pygame.display.update()



def play(pausa,level):
   # sound = pygame.mixer.Sound(r"Sounds\laser5.ogg")
    #pygame.mixer.music.load(r"")
    pygame.mixer.music.set_volume(.25)
    global username
    global music
    
    player_1 = Player(x=0,y=100,speed_walk=4,speed_run=8,gravity=8,jump_power=25,frame_rate_ms=80,move_rate_ms=10,jump_height=150,energia=100,bullets=100,healt=100, live=1)
    lista = load_json_info(JSON_PATH)
    lista_balas = []
   # lista_portales = []
    lista_botines = []
    bulletmanager_1 = BulletManager(player_1.bullets,10000)
    lista_balas = bulletmanager_1.balas_disparadas
    
    # if music == True:
    #     pygame.mixer.music.play(loops=1)
    # else:
    #     pygame.mixer.music.stop()
    
    lista_players = []

    if level == 1:

        imagen_fondo = pygame.image.load(r"Juego_UTN_2024-main\Juego_UTN_2024-main\JUEGO_PARCIAL\resources\background\vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310_640\vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310.jpg")
        imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

        
        lista_players.append(player_1)

       # lista_botines = tomar_objetos(lista['nivel1']['botin'],Botin)

        #lista_portales = tomar_objetos(lista['nivel1']['portal'],Portal)
        
       # lista_botiquines = tomar_objetos(lista['nivel1']['botiquin'],Botiquin)

        lista_enemigos = tomar_enemigo(lista['nivel1']['enemy'])

        #lista_plataformas = tomar_objetos(lista['nivel1']['platform'],Platform)

        #lista_trampas = tomar_objetos(lista['nivel1']['trap'], Trampa)

        

    elif level == 2:
        imagen_fondo = pygame.image.load("resources/background/vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310_640/vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310.jpg")
        imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        lista_players.append(player_1)

        #lista_botines = tomar_objetos(lista['nivel2']['botin'],Botin)

       # lista_portales = tomar_objetos(lista['nivel2']['portal'],Portal)

       # lista_botiquines = tomar_objetos(lista['nivel2']['botiquin'],Botiquin)

        lista_enemigos = tomar_enemigo(lista['nivel2']['enemy'])

       # lista_plataformas = tomar_objetos(lista['nivel2']['platform'],Platform)

        #lista_trampas = tomar_objetos(lista['nivel2']['trap'], Trampa)

        

    elif level == 3:
        imagen_fondo = pygame.image.load("resources/background/vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310_640/vecteezy_2d-game-art-natural-landscape-for-games-mobile_15942310.jpg")
        imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        
        lista_players.append(player_1)

      #  lista_botines = tomar_objetos(lista['nivel3']['botin'],Botin)

        #lista_portales = tomar_objetos(lista['nivel3']['portal'],Portal)

       # lista_botiquines = tomar_objetos(lista['nivel3']['botiquin'],Botiquin)

        lista_enemigos = tomar_enemigo(lista['nivel3']['enemy'])
       
       # lista_plataformas = tomar_objetos(lista['nivel3']['platform'],Platform)

        #lista_trampas = tomar_objetos(lista['nivel3']['trap'], Trampa)

        
    lista_characters = lista_players + lista_enemigos

    pygame.display.set_caption("Jugando")
    while RUNNING:
        keys = pygame.key.get_pressed()  # Obtén el estado actual de las teclas
        if keys[pygame.K_x]:  # Detecta si la tecla está presionada
            bulletmanager_1.shoot(player_1.rect.x, player_1.rect.y + 20, player_1.direction, True)
        elif keys[pygame.K_r]:  # Detecta si la tecla está presionada
            bulletmanager_1.reload()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_ESCAPE:
                    continue  # Aquí podrías pausar el juego en lugar de continuar.

                        


        delta_ms = clock.tick(FPS) 

        
        keys = pygame.key.get_pressed()
        events = pygame.event.get(pygame.KEYDOWN)
        
        texto_energia = fuente.render("Energia: {0}%".format(player_1.energia), True, "White")
        texto_balas = fuente.render("Balas: {0}".format(len(bulletmanager_1.balas_player)), True, "White")
        texto_vida = fuente.render("Vida: {0}".format((player_1.health)), True, "White")
        #texto_score = fuente.render("Score: {0}".format((player_1.score)), True, "White")
       # texto_timer = fuente.render("Tiempo: {0}".format(Timer), True, "Black")
  
    
        
        screen.blit(imagen_fondo,imagen_fondo.get_rect())
        
        '''for botin in lista_botines:
            botin.draw(screen)'''

        ''' for portal in lista_portales:
            portal.draw(screen)'''

        for enemigo in lista_enemigos:
                enemigo.move_enemy(delta_ms,True,bulletmanager_1)
                enemigo.update(delta_ms,lista_plataformas,lista_enemigos,lista_balas)
                enemigo.draw(screen,lista_enemigos)


        '''for plataforma in lista_plataformas:
            plataforma.draw(screen)'''
        '''for botiquin in lista_botiquines:
            botiquin.draw(screen)'''
        
        '''for trampa in lista_trampas:
            trampa.draw(screen)'''

        


        for player in lista_players:
            #if player.win == True:
               # insertar_datos(username,player.score)
               # mostar_ranking()    
            
           # else:

                player.events(keys)
                player.update(delta_ms,lista_plataformas,lista_balas,lista_players)
                player.draw(screen,lista_players)
            
        # if player_1.live == 0 or Timer == 0:
        #     game_over()
        
        screen.blit(texto_energia,(30,30))
        screen.blit(texto_balas,(30,60))
        screen.blit(texto_vida,(30,90))
        #screen.blit(texto_score,(30,120))
        
      #  screen.blit((texto_timer), (725,20))

        
        for bala in bulletmanager_1.balas_disparadas:
                bala.update_bullet(delta_ms,lista_characters,lista_balas)
                bala.draw(screen)

        
        

        pygame.display.flip()
        


def game_over():
    while True:
        screen.blit(Background,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = fuente.render("GAME OVER", True, "Red")
        MENU_RECT = MENU_TEXT.get_rect(center=(750, 300))

        PLAY_BUTTON = Button(image=pygame.image.load("Menu/assets/Play Rect.png"), pos=(750, 400), 
                            text_input="VOLVER A JUGAR", font=fuente, base_color="#d7fcd4", hovering_color="Black")
        QUIT_BUTTON = Button(image=pygame.image.load("Menu/assets/Quit Rect.png"), pos=(750, 550), 
                            text_input="SALIR", font=fuente, base_color="#d7fcd4", hovering_color="Black")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()