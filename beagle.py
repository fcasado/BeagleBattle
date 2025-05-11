import pygame

class Beagle:
    """ Classe para lidar com o personagem Beagle """

    def __init__(self, ai_game):
        """ Inicializa o personagem na tela em sua posição inicial """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Sobe a imagem do beagle
        self.image = pygame.image.load('images/beagle1.bmp')
        self.rect = self.image.get_rect()

        # Começa cada personagem no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Desenha o personagem em sua localização atual """
        self.screen.blit(self.image, self.rect)