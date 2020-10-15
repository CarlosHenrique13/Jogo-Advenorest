import pygame

class Map:
    def __init__(self,grup,janela):
        self.telaGrup = grup
        self.window = janela


    def LoadBack(self):
        # Carrega Senario de Fundo
        bg = pygame.sprite.Sprite(self.telaGrup)
        bg.image = pygame.image.load("data/bgone.png")
        bg.image = pygame.transform.scale(bg.image, [840, 480])
        bg.rect = bg.image.get_rect()
        self.telaGrup.draw(self.window)

    def AnitSky(self):
        # Animação do céu
        pass

    def Ground(self):
        # Geração do Terreno

