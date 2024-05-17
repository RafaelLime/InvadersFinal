from PPlay.sprite import *
from PPlay.window import *

def desenhar_mostros(lin, col, jan_x):
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
    
    


    

# def movimento_v():


def vitoria_monstros(janela, janela_x, janela_y):
    janela.draw_text("GAME OVER", janela_x/2, janela_y/2, size=36, color=(255,255,255))