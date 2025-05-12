import sys
import pygame
from settings import Settings
from beagle import Beagle
from bullet import Bullet
from osso_bullet import OssoBullet
from bad_dog import BadDog

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
        self.bad_dogs = pygame.sprite.Group()

        self._create_pack()

    def run_game(self):
        """ Inicia o loop principal do jogo """
        while True:
            self._check_events()
            self.beagle.update()
            self._update_bullets()
            self._update_bad_dogs()
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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _fire_osso(self):
        """ Cria um novo osso projétil e o adiciona ao grupo projéteis """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_osso_bullet = OssoBullet(self)
            self.bullets.add(new_osso_bullet)

    def _update_bullets(self):
        """ Atualiza a posição dos projéteis e descarta os antigos """
        # Atualiza as posições dos projéteis
        self.bullets.update()

        # Descarta as balas antigas
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Verifica se acertaram o alvo e elimina a bala e o alvo
        collisions = pygame.sprite.groupcollide(self.bullets, self.bad_dogs, True, True)

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
        # Coloca os vilões na tela
        self.bad_dogs.draw(self.screen)       
        # Deixa a tela desenhada mais recente visível
        pygame.display.flip()

    def _create_pack(self):
        """ Cria  a matilha de cães malvadões """

        # Cria um bad dog e adiciona ate preencher a linha usando como distancia o tamanho de um bad_dog
        bad_dog = BadDog(self)
        bad_width, bad_height = bad_dog.rect.size

        current_x, current_y = bad_width, bad_height
        while current_y < (self.settings.screen_height - 3 * bad_height):
            while current_x < (self.settings.screen_width - 2 * bad_width):
                self._create_bad(current_x, current_y)
                current_x += 2 * bad_width
            
            # Termina a fileira, ajusta o x e incrementa o y
            current_x = bad_width
            current_y += 2 * bad_height
           

    def _create_bad(self, x_position, y_position):
        """ Cria um cão malvadão """
        new_bad = BadDog(self)
        new_bad.x = x_position
        new_bad.rect.x = x_position
        new_bad.rect.y = y_position
        self.bad_dogs.add(new_bad)

    def _update_bad_dogs(self):
        """ Verifica se a matillha esta na borda e atualiza as posições de todos os malvadões """
        self._check_bad_pack_edges()
        self.bad_dogs.update()

    def _check_bad_pack_edges(self):
        """ Responde apropriadamente se algum bad_dog chegou na borda da tela """
        for bad_dog in self.bad_dogs.sprites():
            if bad_dog.check_edges():
                self._change_bad_pack_direction()
                break
    
    def _change_bad_pack_direction(self):
        """ Faz toda a frota descer e mudar de direção """
        for bad_dog in self.bad_dogs.sprites():
            bad_dog.rect.y += self.settings.bad_pack_drop_speed
        self.settings.bad_pack_direction *= -1

if __name__ == '__main__':
    # Cria uma instancia do jogo e execute o jogo
    bb = BeagleBattle()
    bb.run_game()
