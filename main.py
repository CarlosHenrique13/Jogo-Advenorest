import pygame
from scr.Screen import Map

# Inicialização pygame
pygame.init()
display = pygame.display.set_mode([840,480])#840 x 480
pygame.display.set_caption("Adventorest")


# Grupos De Colição
senarioGrup = pygame.sprite.Group()
ground = pygame.sprite.Group()


# Classes do Jogo
senario = Map(senarioGrup,display)

# Carega o Background
senario.LoadBack("data/bgone.png")

senario.Ground("data/groundbase.png",ground,0, 420)
senario.Ground("data/groundbase.png",ground,60, 420)


gameLoop = True
clock = pygame.time.Clock()
while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

        pygame.display.update()