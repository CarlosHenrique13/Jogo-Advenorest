import pygame

#Inicialização pygame
pygame.init()
display = pygame.display.set_mode([840,480])#840 x 480
pygame.display.set_caption("Meu Super Jogo 01")

gameLoop = True
clock = pygame.time.Clock()
while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False