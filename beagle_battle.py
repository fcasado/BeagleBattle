import sys
import pygame
from settings import Settings
from beagle import Beagle

class BeagleBattle:
    """ Classe do jogo uma batalha Beagle """
    def __init__(self):
        """ Inicializa o jogo e cria os recursos """
        pygame.init()

        pygame.display.set_caption("Uma Bigada")
        self.clock = pygame.time.Clock()        
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.beagle = Beagle(self)

        # Define a cor de background
        #self.bg_color = (235, 235, 235)
        #self.screen = pygame.display.set_mode((1200, 800))
    

    def run_game(self):
        """ Inicia o loop principal do jogo """
        while True:
            # Observa eventos do teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redesenha a tela durante cada passagem pelo loop
            self.screen.fill(self.settings.bg_color)

            # Coloca o personagem na tela
            self.beagle.blitme()
            
            # Deixa a tela desenhada mais recente visível
            pygame.display.flip()
            self.clock.tick(60)
            

if __name__ == '__main__':
    # Cria uma instancia do jogo e execute o jogo
    bb = BeagleBattle()
    bb.run_game()
