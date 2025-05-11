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

    def run_game(self):
        """ Inicia o loop principal do jogo """
        while True:
            self._check_events()
            self.beagle.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """ Responde as teclas de movimentação e a eventos do mouse """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # move o personagem para a direita                    
                    self.beagle.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.beagle.moving_right = False

    def _update_screen(self):
        """ Atualiza as imagens na tela e muda para a nova tela """
        # Redesenha a tela durante cada passagem pelo loop
        self.screen.fill(self.settings.bg_color)        
        # Coloca o personagem na tela
        self.beagle.blitme()        
        # Deixa a tela desenhada mais recente visível
        pygame.display.flip()
        

if __name__ == '__main__':
    # Cria uma instancia do jogo e execute o jogo
    bb = BeagleBattle()
    bb.run_game()
