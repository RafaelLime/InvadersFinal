from math import floor

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

def mostrar(janela,lista,Screen_W):

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
