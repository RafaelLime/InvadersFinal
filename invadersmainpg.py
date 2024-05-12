from PPlay.window import *
import pygame
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.sprite import *
from PPlay.keyboard import *

pygame.init()



#Janela e Fundo:
Screen_W = 1000
Screen_H = 700
janela = Window(Screen_W, Screen_H)
fundo = GameImage("Sprites/menu.jpg")
janela.set_title("SpaceInvaders - Pedro Guedes")

seta = GameImage("Sprites/seta.jpg")
seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) - 80)

janela.set_background_color([0, 0, 0])

teclado = Window.get_keyboard()


def play(dificult = 2):

    tiros = []
    nave = Sprite("Sprites/nave2.png")
    nave.set_position(Screen_W/2, Screen_H - 100)
    reload = 0
    atirou = True
    # Esse comentário só vai aparecer na jogabilidade

    while True:
        

        janela.set_background_color([0, 0, 0])
        nave.draw()

        # Movimento da nave
        if (teclado.key_pressed("left") and nave.x > 0):
            nave.x = nave.x - 150*janela.delta_time() + dificult*20*janela.delta_time()
        elif (teclado.key_pressed("right") and nave.x < Screen_W - nave.width):
            nave.x = nave.x + 150*janela.delta_time() - dificult*20*janela.delta_time()
        
        # Tiros
        # Se a tecla espaço está pressionada criar novo tiro
        if (teclado.key_pressed("space") and reload <= 0):
            tiro = Sprite("Sprites/tirog.png")
            tiro.set_position(nave.x+nave.width/2, nave.y)
            reload = 0.3
            tiros.append(tiro)
        
        for tiro in tiros:
            tiro.draw()
            tiro.y -= 100*janela.delta_time()
            if (tiro.y < 0):
                del tiro

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        if (reload < 0):
            reload = 0
        else:
            reload -= janela.delta_time()
        janela.update()
    
def dificuldade():
    while True:
        
        janela.set_background_color([0, 0, 0])

        janela.draw_text(text='Facil', x= (Screen_W / 2)
                     , y= 20, size= 24, color=(255,255,255), font_name="Arial")
        janela.draw_text(text='Normal', x= (Screen_W / 2)
                     , y= 60, size= 24, color=(255,255,255), font_name="Arial")
        janela.draw_text(text='Hard', x= (Screen_W / 2)
                     , y= 100, size= 24, color=(255,255,255), font_name="Arial")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        janela.update()

#def ranking():
    

def main_menu():

    GameState = 0

    while True:
        
        janela.set_background_color([0, 0, 0])     


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        if teclado.key_pressed("S"):
            GameState += 1
                    
        if teclado.key_pressed("W"):
            GameState -= 1
            

        if GameState == 0 and teclado.key_pressed("ENTER"):
            play()
        if GameState == 1 and teclado.key_pressed("ENTER"):
            dificuldade()
                
        if GameState == 3 and teclado.key_pressed("ENTER"):
            pygame.quit()
            sys.exit()
                    

        if GameState == 0:
            seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) - 80)
        if GameState == 1:
            seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) + 20)
        if GameState == 2:
            seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) + 120)
        if GameState == 3:
            seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) + 220)
        
        


        if GameState > 3:
            GameState = 0
            seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) - 80)
        if GameState < 0:
           GameState = 3
           seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) + 320)

        
        fundo.draw()
        seta.draw()


        janela.update()
        

main_menu()
