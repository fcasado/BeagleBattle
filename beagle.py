import pygame

class Beagle:
    """ Classe para lidar com o personagem Beagle """

    def __init__(self, bb_game):
        """ Inicializa o personagem na tela em sua posição inicial """
        self.screen = bb_game.screen
        self.settings = bb_game.settings
        self.screen_rect = bb_game.screen.get_rect()

        # Sobe a imagem do beagle
        self.image = pygame.image.load('images/beagle3.bmp')
        self.rect = self.image.get_rect()

        # Começa cada personagem no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # armazena um float para a posição horizontal exata do beagle
        self.x = float(self.rect.x)

        # Flag de movimento; começa com um beagle parado
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Atualizar a posição do Beagle com base na flag de movimento """
        # Atualiza o valor de x do beagle, não o rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.beagle_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.beagle_speed

        # Atualiza o objeto rect de self.x
        self.rect.x = self.x 

    def blitme(self):
        """ Desenha o personagem em sua localização atual """
        self.screen.blit(self.image, self.rect)

    def center_beagle(self):
        """ Centraliza o Beagle na tela """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)