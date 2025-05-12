import pygame
from pygame.sprite import Sprite

class OssoBullet(Sprite):
    """ Classe para gerenciar o osso bala lançado pelo Beagle """
    
    def __init__(self, bb_game):
        """ Cria um objeto osso-bala na posição do Beagle """
        super().__init__()
        self.screen = bb_game.screen
        self.settings = bb_game.settings
        self.image = pygame.image.load('images/osso.bmp')

        # Cria um bullet rect em (0,0) e em seguida, define a posição correta
        self.rect = self.image.get_rect()
        #self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = bb_game.beagle.rect.midtop

        # Armazena a posição do projétil como float
        self.y = float(self.rect.y)
    
    def update(self):
        """ Desloca o projetil verticalmente pela tela """
        # Atualiza a posição exata do projétil
        self.y -= self.settings.bullet_speed
        # Atualiza a posição do rect
        self.rect.y = self.y

    def draw_bullet(self):
        """ Desenha a bala na tela """
        #pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)