import pygame
from pygame.sprite import Sprite

class BadDog(Sprite):
    """ Classe para representar um cão bravo baddog """

    def __init__(self, bb_game):
        """ Inicializa o bad dog e define a posição inicial """
        super().__init__()
        self.screen = bb_game.screen

        # Carrega a imagem do cão malvadão e define seu atributo rect
        self.image = pygame.image.load('images/angry_dog2.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada bad dog novo perto do canto superior esquerdo
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal exata do malvadão.. :(
        self.x  = float(self.rect.x)