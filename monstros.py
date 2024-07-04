from PPlay.sprite import *
from PPlay.window import *

def desenhar_mostros(lin, col:int, jan_x:Window):
    # matriz de monstros
    monstro = []
    for i in range(lin):
        monstro.append([])
    
    for i in range(lin):
        for j in range(col):
            monster = Sprite("Sprites/invader.png")
            monster.set_position(jan_x/2 -col*monster.width + j*monster.width, 25 + i*monster.height)
            monstro[i].append(monster)
    
    for i in range(lin):
        for j in range(col):
            monstro[i][j].draw()
    
    return monstro


def vitoria_monstros(janela:Window, janela_x, janela_y):
    janela.draw_text("GAME OVER", janela_x/2, janela_y/2, size=36, color=(255,255,255))

def colisaoMostroEscudo(monstro:Sprite, escudos:list):
    for escudo in escudos:
        if monstro.collided(escudo):
            return True
    return False
