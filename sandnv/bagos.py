import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
largura = 800
altura = 600

# Define a cor do círculo e do fundo
cor_circulo = (155, 0, 0)   # Vermelho
cor_fundo = (0, 0, 0)      # Preto

# Cria a janela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Círculo segue o cursor do mouse')

# Define o raio do círculo
raio_circulo = 30

# Loop principal do jogo
while True:
    # Processa os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtém a posição do cursor do mouse
    x_mouse, y_mouse = pygame.mouse.get_pos()

    # Atualiza a tela
    tela.fill(cor_fundo)
    pygame.draw.circle(tela, cor_circulo, (x_mouse, y_mouse), raio_circulo)
    pygame.display.flip()

    # Define a taxa de atualização do jogo
    pygame.time.Clock().tick(30)