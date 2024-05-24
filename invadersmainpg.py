from PPlay.window import *
import pygame
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.sprite import *
from PPlay.keyboard import *
from monstros import *
from PPlay.animation import *

pygame.init()



#Janela e Fundo:
Screen_W = 1000
Screen_H = 700
janela = Window(Screen_W, Screen_H)
fundo = GameImage("Sprites/menu.jpg")
janela.set_title("SpaceInvaders - Rafael Lima")

seta = GameImage("Sprites/seta.jpg")
seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) - 80)

janela.set_background_color([0, 0, 0])

teclado = Window.get_keyboard()




def play(dificult = 2):

    tiros = []
    nave = Sprite("Sprites/nave2.png")
    nave.set_position(Screen_W/2, Screen_H - 100)
    reload = 0
    # Linhas e colunas de monstros
    lin = 3
    col = 5
    mobs = 0
    score = 0
    velocidade_x = 250
    velocidade_y = 75
    # Monstros (Inimigos)
    matriz_inimigos = desenhar_mostros(lin, col, Screen_W)

    while True:
        

        janela.set_background_color([0, 0, 0])
        nave.draw()
        janela.draw_text(f"Pontuação: {int(score)}", x=Screen_W - 180, y=20, size=24, color=(255, 255, 255))

        if mobs == lin * col:
            score += (200 - janela.time_elapsed()/1000)*10
            print(f"Sua pontuação na partida: {int(score)}pts")
            break
        
        # Movimentação dos monstros
        for linha in matriz_inimigos:
            for monstro in linha:

                # Vitória dos monstros
                if monstro.y >= nave.y:
                    vitoria_monstros(janela, Screen_W, Screen_H)
                
                monstro.x += velocidade_x * janela.delta_time()
                monstro.draw()
                if (monstro.x <= 0 or monstro.x + 40 >= Screen_W):
                    # Movimento vertical
                    for linha in matriz_inimigos:
                        for monstro in linha:
                            monstro.x -= velocidade_x * janela.delta_time()
                            monstro.y += velocidade_y
                    
                    velocidade_x *= -1
                
                # Colisão dos monstros com tiro
                for tiro in tiros:
                    if tiro.y < monstro.y or tiro.x < monstro.x:
                        continue
                    else:
                        if (monstro.collided(tiro)):
                            linha.remove(monstro)
                            tiros.remove(tiro)
                            mobs += 1
                            score += 100
                            break
                        
                

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
            tiro.y -= 250*janela.delta_time()
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
        

        # Condição para vitória dos monstros
        # if (matriz_inimigos[lin-1][0].y >= nave.y):
        #     vitoria_monstros(janela, Screen_W, Screen_H)

        # Cálculo do FPS
        # print(f"FPS: {1/janela.delta_time()*1000}")

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
