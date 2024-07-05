from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *
from random import randint
from math import trunc

def movimento_nave(janela:Window, teclado:Keyboard, nave:Sprite, Screen_W:int, dificult:int) -> Sprite:
    if (teclado.key_pressed("left") and nave.x > 0):
        nave.x = nave.x - 150*janela.delta_time() + dificult*20*janela.delta_time()
    elif (teclado.key_pressed("right") and nave.x < Screen_W - nave.width):
        nave.x = nave.x + 150*janela.delta_time() - dificult*20*janela.delta_time()
    return nave

def desenhar_escudos(Screen_H, Screen_W):
    shields = []
    for i in range(4):
        shield = Sprite("Sprites/escuro_inteiro.png")
        shield.set_position((Screen_W - 250*i) - shield.width - 100, Screen_H - 150)
        shields.append(shield)
    return shields

def updateEscudos(shields) -> None:
    for i in shields:
        i.draw()

def desenharNave(janela, nave:Sprite, time_inv, invencivel):
    if invencivel:
        time_inv -= janela.delta_time()
        if bool(randint(0,1)):
            nave.draw()
    
        if time_inv <= 0:
            time_inv = 0
            invencivel = False
    else:
        nave.draw()
    return time_inv,nave,invencivel

def criar_tiro(teclado, tiros, nave, reload, rep):
    if (teclado.key_pressed("space") and reload <= 0):
        rep += 1
        tiro = Sprite("Sprites/tirog.png")
        tiro.set_position(nave.x+nave.width/2, nave.y)
        reload = 0.3
        tiros.append(tiro)
    return tiros, reload, rep

def movimentar_tiros(janela:Window, tiros):
    for tiro in tiros:
        tiro.draw()
        tiro.y -= 325*janela.delta_time()
        if (tiro.y < 0):
            del tiro
    return tiros

def updateReloads(janela:Window, reload, m_reload):
    if (reload < 0):
        reload = 0
    else:
        reload -= janela.delta_time()
    
    if (m_reload < 0):
        m_reload = 0
    else:
        m_reload -= janela.delta_time()
    return reload, m_reload

def game_over(score:float, janela, teclado, Screen_W, Screen_H):
    janela.set_background_color([0, 0, 0])
    while True:
        janela.draw_text("GAME OVER",Screen_W/3 + 100, Screen_H/2 - 40, size=36, color=([255, 255, 255]))
        janela.draw_text(f"Pontuação: {trunc(score)}",Screen_W/3 - 40, Screen_H/2 + 80, size=36, color=([255, 255, 255]))
        janela.draw_text(f"Pressione espaço para voltar ao menu",Screen_W/3 - 40, Screen_H/2 + 120, size=36, color=([255, 255, 255]))
        if teclado.key_pressed("space"):
            break
        janela.update()
    
    return

def ColisaoTiroEscudo(tiro:Sprite, tiros:list, escudos:list) -> list:
    for escudo in escudos:
        if tiro.collided(escudo):
            tiros.remove(tiro)
            break
    return tiros
