import sys
import pygame
from settings import Settings
from beagle import Beagle
from bullet import Bullet
from osso_bullet import OssoBullet

class BeagleBattle:
    """ Classe do jogo uma batalha Beagle """
    def __init__(self):
        """ Inicializa o jogo e cria os recursos """
        pygame.init()
        self.settings = Settings()

        # Tela cheia
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        # Tela 1200x800 - Vide settings
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        
        pygame.display.set_caption("Uma Bigada")
        self.clock = pygame.time.Clock()
                
        self.beagle = Beagle(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """ Inicia o loop principal do jogo """
        while True:
            self._check_events()
            self.beagle.update()
            self.bullets.update()

            # Descarta as balas perdidas
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                print(len(self.bullets))

            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """ Responde as teclas de movimentação e a eventos do mouse """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Responde a teclas pressionadas """
        if event.key == pygame.K_RIGHT:
            # move o personagem para a direita                    
            self.beagle.moving_right = True
        elif event.key == pygame.K_LEFT:
            # move o beagle para a esquerda
            self.beagle.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_c:
            self._fire_bullet()
        elif event.key == pygame.K_SPACE:
            self._fire_osso()

    def _check_keyup_events(self, event):
        """ Responde a teclas soltas """
        if event.key == pygame.K_RIGHT:
            self.beagle.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.beagle.moving_left = False
    
    def _fire_bullet(self):
        """ Cria um novo projétil e o adiciona ao grupo projéteis """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _fire_osso(self):
        """ Cria um novo osso projétil e o adiciona ao grupo projéteis """
        new_osso_bullet = OssoBullet(self)
        self.bullets.add(new_osso_bullet)

    def _update_screen(self):
        """ Atualiza as imagens na tela e muda para a nova tela """
        # Redesenha a tela durante cada passagem pelo loop
        self.screen.fill(self.settings.bg_color)
        # Mostra as balas
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Mostra os ossos
        for osso_bullet in self.bullets.sprites():
            osso_bullet.draw_bullet()
        # Coloca o personagem na tela
        self.beagle.blitme()        
        # Deixa a tela desenhada mais recente visível
        pygame.display.flip()
        

if __name__ == '__main__':
    # Cria uma instancia do jogo e execute o jogo
    bb = BeagleBattle()
    bb.run_game()
