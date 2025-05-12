import pygame
from pygame.sprite import Sprite

class BadDog(Sprite):
    """ Classe para representar um cão bravo baddog """

    def __init__(self, bb_game):
        """ Inicializa o bad dog e define a posição inicial """
        super().__init__()
        self.screen = bb_game.screen
        self.settings = bb_game.settings

        # Carrega a imagem do cão malvadão e define seu atributo rect
        self.image = pygame.image.load('images/angry_dog2a.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada bad dog novo perto do canto superior esquerdo
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal exata do malvadão.. :(
        self.x  = float(self.rect.x)

    def update(self):
        """ Move os malvadões para a direita ou para a esquerda """
        self.x += self.settings.bad_speed * self.settings.bad_pack_direction
        self.rect.x = self.x

    def check_edges(self):
        """ Retorna True se o bad_dog estiver na borda da tela """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)