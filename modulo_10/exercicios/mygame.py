from PIL import ImageColor
from pygame import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_s, K_j
from pygame import display, init, font, draw, event
from sys import exit
init()

branco = ImageColor.getrgb('white')
amarelo = ImageColor.getrgb('yellow')
preto = ImageColor.getrgb('black')
vermelho = ImageColor.getrgb('red')
verde = ImageColor.getrgb('green')
azul = ImageColor.getrgb('blue')

largura = 600
altura = 400
dis = display.set_mode((largura, altura))
display.set_caption('My Game')

def jogo():

    x_bola = 295
    y_bola = 250
    x_base = 150
    y_base = 390
    largura_base = 300
    comprimento_base = 1
    x_base_change = 0
    x_bola_change = -0.05
    y_bola_change = -0.05
    
    message = lambda m, c, pos : dis.blit(
        font.SysFont('Segoe UI', 25).render(m, True,c), pos
    )

    pontos = 0
    
    while True:
        while y_bola > altura:
            dis.fill(vermelho)
            message('game over', vermelho, [250, 60])
            message('J para jogar e S para sair', preto, [50, 100])
            display.update()
    
            for e in event.get():
                if e.type == QUIT:
                    exit()
                if e.type == KEYDOWN:
                    if e.key == K_s:
                       exit()
                    elif e.key == K_j:
                        jogo()

        for e in event.get():
            if e.type == QUIT:
                exit()
            if e.type == KEYDOWN:
                if e.key == K_s:
                    exit()
                elif e.key == K_RIGHT:
                    if x_base + 300 < largura: 
                        x_base_change = 10
                        x_base += x_base_change
                elif e.key == K_LEFT:
                    if x_base > 0:
                        x_base_change = -10
                        x_base += x_base_change
    
        if x_bola < 0 or x_bola > largura -10:
            x_bola_change = -x_bola_change
        elif y_bola < 0:
            y_bola_change = -y_bola_change
        elif y_bola >= y_base - 10 and x_bola >= x_base and x_bola <= x_base + 300:
            y_bola_change = -y_bola_change
            
    
        x_bola += x_bola_change
        y_bola += y_bola_change
        posicao_bola = [x_bola, y_bola, 10, 10]
    
        dis.fill(preto)
        draw.rect(dis, verde, [x_base, y_base, largura_base, comprimento_base])
        draw.rect(dis, verde, posicao_bola, 10, border_radius=10)
            
        display.update()

jogo()
