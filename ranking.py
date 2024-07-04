from math import floor
from PPlay.mouse import *
from PPlay.window import *
from PPlay.gameimage import *

class Pontuador:
    def __init__(self,nome,pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao

def registrar(nome,pontuacao):
    with open("highscore.txt", "a", encoding="utf-8") as arq:
        arq.write(f"{nome}: {floor(pontuacao)}\n")

def consultar():
    rank = []
    with open("highscore.txt", "r", encoding="utf-8") as arq:
        for linha in arq:
            infos = linha.split()
            rank.append(Pontuador(infos[0], int(infos[1])))
        rank.sort(key=lambda x:x.pontuacao,reverse=True)
        return rank

def mostrar(janela:Window,lista,Screen_W):

    janela.draw_text(text=f'{lista[0].nome} {lista[0].pontuacao}', x= (Screen_W / 2)
                     , y= 100, size= 24, color=(255,255,255), font_name="Arial")
    janela.draw_text(text=f'{lista[1].nome} {lista[1].pontuacao}', x= (Screen_W / 2)
                     , y= 125, size= 24, color=(255,255,255), font_name="Arial")
    janela.draw_text(text=f'{lista[2].nome} {lista[2].pontuacao}', x= (Screen_W / 2)
                     , y= 150, size= 24, color=(255,255,255), font_name="Arial")
    janela.draw_text(text=f'{lista[3].nome} {lista[3].pontuacao}', x= (Screen_W / 2)
                     , y= 175, size= 24, color=(255,255,255), font_name="Arial")
    janela.draw_text(text=f'{lista[4].nome} {lista[4].pontuacao}', x= (Screen_W / 2)
                     , y= 200, size= 24, color=(255,255,255), font_name="Arial")

def ranking(janela, teclado, Screen_W) -> None:
    
    lista = consultar()
    while True:
        janela.set_background_color([0,0,0])
        mostrar(janela,lista,Screen_W)
        if teclado.key_pressed("ESC"):
            break
        janela.update()
    return

# Outras janelas
def SetGameState(mouse:Mouse) -> int:
    if mouse.is_over_area([460,280],[760,325]):
        return 0
    elif mouse.is_over_area([460,380],[760,425]):
        return 1
    elif mouse.is_over_area([460,480],[760,525]):
        return 2       
    elif mouse.is_over_area([460,580],[760,625]):
        return 3

def SetPositionSeta(GameState:int, seta:GameImage, Screen_W:int, Screen_H:int) -> GameImage:
    if GameState == 0:
        seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) - 80)
    elif GameState == 1:
        seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) + 20)
    elif GameState == 2:
        seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) + 120)
    elif GameState == 3:
        seta.set_position((Screen_W / 2)- 300, (Screen_H / 2) + 220)
    
    return seta
