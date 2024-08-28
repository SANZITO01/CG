import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define a tela
screen = pygame.display.set_mode((800, 600))

# Configura o relógio
clock = pygame.time.Clock()

# Define uma taxa constante de 60 FPS
FPS = 60

# Definindo a posição inicial do círculo
x_position = 400
y_position = 300
speed = 300  # velocidade em pixels por segundo

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Obtém o tempo passado desde o último frame em segundos
    delta_time = clock.tick(FPS) / 1000.0
    
    # Atualiza a lógica do jogo aqui usando delta_time para velocidade constante
    x_position += speed * delta_time
    
    # Reverte a direção ao atingir as bordas da tela
    if x_position > 800 or x_position < 0:
        speed = -speed
    
    # Desenha na tela aqui
    screen.fill((0, 0, 0))  # Limpa a tela com a cor preta
    pygame.draw.circle(screen, (255, 0, 0), (int(x_position), y_position), 30)  # Desenha um círculo vermelho
    
    # Atualiza o display
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
sys.exit()