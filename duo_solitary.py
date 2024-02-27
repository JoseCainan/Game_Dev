import pygame
import random

pygame.init()
# titulo da janela do pygane, e definição de largura e altura
pygame.display.set_caption("jogo da cobra")
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# definindo cores para simplificar
preto = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
roza = (255, 128, 192)

# tamanho da cobra ( ou seja tamanho do quadrado) / abaixo, abaixo velocidade da cobra
tamanho_quad = 10
velocidade_game = 12

# Funçoes para POE - programação orientada a evento
def velocidade_evento(tecla):
    velocidade_x, velocidade_y = 0, 0
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quad
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quad
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quad
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quad
        velocidade_y = 0

    return velocidade_x, velocidade_y

def velocidade_evento2(tecla):
    velocidade_x, velocidade_y = 0, 0
    if tecla == pygame.K_s:
        velocidade_x = 0
        velocidade_y = tamanho_quad
    elif tecla == pygame.K_w:
        velocidade_x = 0
        velocidade_y = -tamanho_quad
    elif tecla == pygame.K_d:
        velocidade_x = tamanho_quad
        velocidade_y = 0
    elif tecla == pygame.K_a:
        velocidade_x = -tamanho_quad
        velocidade_y = 0

    return velocidade_x, velocidade_y

def rand_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quad) / 10) * 10
    comida_y = round(random.randrange(0, altura - tamanho_quad) / 10) * 10
    return comida_x, comida_y

def mostrar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def mostrar_cobra2(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, roza, [pixel[0], pixel[1], tamanho, tamanho])

def mostra_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho, tamanho])

def pontuacao(ponto, cor, posicao):
    fonte = pygame.font.SysFont('Helvetica', 25)
    text = fonte.render(f'Pontos: {ponto}', True, cor)
    tela.blit(text, posicao)

def rodar_jogo():
    game_over1 = False
    game_over2 = False

    x1, y1 = largura / 4, altura / 2
    x2, y2 = 3 * largura / 4, altura / 2

    velo_x1, velo_y1 = 0, 0
    velo_x2, velo_y2 = 0, 0

    tamanho_cobra1 = 1
    tamanho_cobra2 = 1

    pixels1 = []
    pixels2 = []

    comida_x, comida_y = rand_comida()

    while not (game_over1 and game_over2):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over1 = True
                game_over2 = True
            elif evento.type == pygame.KEYDOWN:
                # Controle da cobra 1
                if evento.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT]:
                    velo_x1, velo_y1 = velocidade_evento(evento.key)

                # Controle da cobra 2
                if evento.key in [pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a]:
                    velo_x2, velo_y2 = velocidade_evento2(evento.key)

        x1 += velo_x1
        y1 += velo_y1
        pixels1.append([x1, y1])
        if len(pixels1) > tamanho_cobra1:
            del pixels1[0]

        if (
            x1 < 0 or x1 >= largura or
            y1 < 0 or y1 >= altura or
            [x1, y1] in pixels1[:-1] or
            [x1, y1] == [x2, y2]
        ):
            game_over1 = True

        if x1 == comida_x and y1 == comida_y:
            tamanho_cobra1 += 1
            comida_x, comida_y = rand_comida()

        x2 += velo_x2
        y2 += velo_y2
        pixels2.append([x2, y2])
        if len(pixels2) > tamanho_cobra2:
            del pixels2[0]

        if (
            x2 < 0 or x2 >= largura or
            y2 < 0 or y2 >= altura or
            [x2, y2] in pixels2[:-1] or
            [x2, y2] == [x1, y1]
        ):
            game_over2 = True

        if x2 == comida_x and y2 == comida_y:
            tamanho_cobra2 += 1
            comida_x, comida_y = rand_comida()

        tela.fill(preto)
        mostra_comida(tamanho_quad, comida_x, comida_y)
        mostrar_cobra(tamanho_quad, pixels1)
        mostrar_cobra2(tamanho_quad, pixels2)
        pontuacao(tamanho_cobra1 - 1, verde, [1, 1])
        pontuacao(tamanho_cobra2 - 1, azul, [largura // 2 + 1, 1])

        pygame.display.update()
        relogio.tick(velocidade_game)

    pygame.quit()

if __name__ == '__main__':
    rodar_jogo()