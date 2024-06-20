from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *

def movimento_nave(janela, teclado, nave, Screen_W, dificult):
    if (teclado.key_pressed("left") and nave.x > 0):
        nave.x = nave.x - 150*janela.delta_time() + dificult*20*janela.delta_time()
    elif (teclado.key_pressed("right") and nave.x < Screen_W - nave.width):
        nave.x = nave.x + 150*janela.delta_time() - dificult*20*janela.delta_time()
    return nave

def criar_tiro(teclado, tiros, nave, reload):
    if (teclado.key_pressed("space") and reload <= 0):
            tiro = Sprite("Sprites/tirog.png")
            tiro.set_position(nave.x+nave.width/2, nave.y)
            reload = 0.3
            tiros.append(tiro)
    return tiros, reload

def movimentar_tiros(janela, tiros):
    for tiro in tiros:
        tiro.draw()
        tiro.y -= 250*janela.delta_time()
        if (tiro.y < 0):
            del tiro
    return tiros
