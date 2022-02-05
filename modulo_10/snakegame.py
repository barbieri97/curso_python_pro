
from pygame import display, init, time as pytime, font, draw, event, quit as pyquit
from pygame import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_UP, K_s, K_j
import random
from PIL import ImageColor
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
display.set_caption('Snake Game')

clock = pytime.Clock()

snake_body = 10

score = lambda s : dis.blit(
    font.SysFont('arial.ttf', 35).render(f'pontuação: {s - 1}', True, azul), [0,0]
)

message = lambda m, c, pos : dis.blit(
    font.SysFont('Segoe UI', 25).render(m, True,c), pos
)

criar_comida = lambda esp, pos : round(random.randrange(esp, pos - 10) / 10) * 10

def jogo():
    game_over = False
    fechar = False

    x1 = largura / 2
    y1 = largura / 2

    x1_change = 0
    y1_change = 0

    corpo = []
    tamanho = 1
    level = 10

    comida_x = criar_comida(0, largura)
    comida_y = criar_comida(30, altura)

    while not game_over:
        while fechar:
            dis.fill(branco)
            message('game over', vermelho, [250, 60])
            message('J para jogar e S para sair', preto, [50, 100])
            score(tamanho)
            display.update()

            for e in event.get():
                    if e.type == KEYDOWN:
                        if e.key == K_s:
                            exit()
                        if e.key == K_j:
                            jogo()

        for e in event.get():
            if e.type == QUIT:
                game_over = True
            if e.type == KEYDOWN:
                if e.key == K_LEFT:
                    x1_change = -snake_body
                    y1_change = 0
                elif e.key == K_RIGHT:
                    x1_change = snake_body
                    y1_change = 0
                elif e.key == K_UP:
                    y1_change = -snake_body
                    x1_change = 0
                elif e.key == K_DOWN:
                    y1_change = snake_body
                    x1_change = 0

        if any([x1 >= largura, x1 < 0, y1 >= altura, y1 < 0]):
            fechar = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(branco)
        draw.rect(dis, vermelho, [comida_x, comida_y, snake_body, snake_body])
        cabeca = []
        cabeca.append(x1)
        cabeca.append(y1)
        corpo.append(cabeca)
        if len(corpo) > tamanho:
            del corpo[0]

        for x in corpo[:-1]:
            if x == cabeca:
                fechar = True
        
        [draw.rect(dis, verde, [x[0], x[1], snake_body, snake_body]) for x in corpo]
        display.update

        if x1 == comida_x and y1 == comida_y:
            comida_x = criar_comida(0, largura)
            comida_y = criar_comida(30, altura)
            tamanho += 1
            level += 2

        clock.tick(level)
    pyquit()
    quit()

jogo()