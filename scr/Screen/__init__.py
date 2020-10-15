import pygame

class Map:
    def __init__(self,grup,janela):
        self.telaGrup = grup
        self.window = janela


    def LoadBack(self,img):
        # Carrega Senario de Fundo
        bg = pygame.sprite.Sprite(self.telaGrup)
        bg.image = pygame.image.load(img)
        bg.image = pygame.transform.scale(bg.image, [840, 480])
        bg.rect = bg.image.get_rect()
        self.telaGrup.draw(self.window)

    def AnitSky(self):
        # Animação do céu
        pass

    def Ground(self,img,grup,x,y):
        # Geração do Terreno
        ground = pygame.sprite.Sprite(grup)
        ground.image = pygame.image.load(img)
        ground.image = pygame.transform.scale(ground.image, [60, 60])
        ground.rect = pygame.Rect(x,y, 60, 60)

        grup.draw(self.window)


