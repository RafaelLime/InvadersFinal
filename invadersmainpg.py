from PPlay.window import *
import pygame
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.mouse import *
from monstros import *
from PPlay.animation import *
from random import choice
from ranking import *
from game import *

pygame.init()



#Janela e Fundo:
Screen_W, Screen_H = 1000, 700

janela = Window(Screen_W, Screen_H)
fundo = GameImage("Sprites/menu.jpg")
janela.set_title("SpaceInvaders - Rafael Lima")



janela.set_background_color([0, 0, 0])

teclado = Window.get_keyboard()
mouse = Window.get_mouse()
lin, col, score, hp = 3, 5, 0, 3




def play(dificult = 2):
    global score
    global hp

    tiros = []
    tiros_mostro = []
    shields = desenhar_escudos(Screen_H, Screen_W)
    nave = Sprite("Sprites/nave2.png")
    nave.set_position(Screen_W/2, Screen_H - 100)
    reload = 0
    m_reload = 0
    
    mobs = 0
    
    velocidade_x = 125
    velocidade_y = 75
    
    invencivel = False
    time_inv = 0
    atingiu = False
    # Monstros (Inimigos)
    matriz_inimigos = desenhar_mostros(lin, col, Screen_W)

    while True:
        

        janela.set_background_color([0, 0, 0])
        janela.draw_text(f"Pontuação: {int(score)}", x=Screen_W - 180, y=20, size=24, color=(255, 255, 255))
        janela.draw_text(f"Hp: {hp}", x=20, y=20, size=24, color=(255, 255, 255))

        if mobs == lin * col:
            score += (200 - janela.time_elapsed()/1000)*10
            print(f"Sua pontuação na partida: {int(score)}pts")
            break
        
        # Desenhar nave
        time_inv, nave, invencivel = desenharNave(janela, nave, time_inv, invencivel)

        # Desenhar escudos
        updateEscudos(shields)
        

        # Movimentação dos monstros
        for linha in matriz_inimigos:
            if len(linha) != 0:
                atira = choice(linha)
            for monstro in linha:
                if monstro == atira and m_reload <= 0:
                    tiros_mostro, m_reload = CriaTiroMonstro(monstro, tiros_mostro)


                # Vitória dos monstros
                if colisaoMostroEscudo(monstro, shields):    
                    vitoria_monstros(janela, Screen_W, Screen_H)
                    return 0
                
                monstro = MovimentoHorizontalMonstro(monstro, velocidade_x, janela)
                if (monstro.x <= 0 or monstro.x + 40 >= Screen_W):
                    # Movimento vertical
                    matriz_inimigos = MovimentoVerticalMonstros(matriz_inimigos, janela, velocidade_x, velocidade_y)
                    
                    velocidade_x *= -1
                
                # Colisão dos monstros com tiro
                for tiro in tiros:
                    tiros = ColisaoTiroEscudo(tiro, tiros, shields)

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
        nave = movimento_nave(janela, teclado, nave, Screen_W, dificult)
        
        # Tiros
        # Se a tecla espaço está pressionada criar novo tiro
        tiros, reload = criar_tiro(teclado, tiros, nave, reload)
        
        tiros = movimentar_tiros(janela, tiros)

        for projetil in tiros_mostro:
            projetil.draw()
            projetil.y += 250*janela.delta_time()
            if nave.collided(projetil) and not invencivel:
                # Dano ao player
                hp -= 1
                invencivel = True
                time_inv = 2
                nave.set_position(Screen_W/2, Screen_H - 100)
                atingiu = True
                if hp == 0:
                    score += (200 - janela.time_elapsed()/1000)*10
                    nome = input("Digite seu nome para registro: ")
                    registrar(nome,score)
                    return 0
                    
                    
                
            if projetil.y > Screen_H or atingiu:
                tiros_mostro.remove(projetil)
                atingiu = False
            
            for escud in shields:
                if projetil.collided(escud):
                    if escud.height <= 4:
                        shields.remove(escud)
                    else:
                        escud.height -= 3
                        escud.y += 3
                    tiros_mostro.remove(projetil)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        # Atualização dos reloads
        reload, m_reload = updateReloads(janela, reload, m_reload)
        

        # Cálculo do FPS
        # print(f"FPS: {1/janela.delta_time()*1000}")

        janela.update()
    
    return 1
    
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



    

def main_menu():
    seta = GameImage("Sprites/seta.jpg")
    seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) - 80)

    GameState = 0

    while True:
        
        janela.set_background_color([0, 0, 0])     


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            
        if mouse.is_over_area([460,280],[760,325]):
            GameState = 0
        elif mouse.is_over_area([460,380],[760,425]):
            GameState = 1
        elif mouse.is_over_area([460,480],[760,525]):
            GameState = 2    
        elif mouse.is_over_area([460,580],[760,625]):
            GameState = 3
            

        if mouse.is_over_area([460,280],[760,325]) and mouse.is_button_pressed(1):
            return 1
        if mouse.is_over_area([460,380],[760,425]) and mouse.is_button_pressed(1):
            dificuldade()
        if mouse.is_over_area([460,480],[760,525]) and mouse.is_button_pressed(1):
            ranking(janela, teclado, Screen_W)        
        if mouse.is_over_area([460,580],[760,625]) and mouse.is_button_pressed(1):
            pygame.quit()
            sys.exit()
                    

        seta = SetPositionSeta(GameState, seta, Screen_W, Screen_H)
              
        fundo.draw()
        seta.draw()


        janela.update()


if main_menu() == 1:
    diff = 2
    while True:
        if play(diff) == 0:
            break
        col += 1
        diff += 0.2

    game_over(score, janela, teclado, Screen_W, Screen_H)
    main_menu()
