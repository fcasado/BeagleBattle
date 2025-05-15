import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from beagle import Beagle
from bullet import Bullet
from osso_bullet import OssoBullet
from bad_dog import BadDog
from button import Button

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
        
        # Cria uma instancia para armazenar as estatisticas do jogo
        self.stats = GameStats(self)

        self.clock = pygame.time.Clock()
        
        self.beagle = Beagle(self)
        self.bullets = pygame.sprite.Group()
        self.bad_dogs = pygame.sprite.Group()

        self._create_pack()

        # Inicializa o jogo em um estado inativo
        self.game_active = False

        # Cria o botão Play
        self.play_button = Button(self, "Jogar")

    def run_game(self):
        """ Inicia o loop principal do jogo """
        while True:
            self._check_events()
            if self.game_active:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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
        elif event.key == pygame.K_j:
            # Inicia a Jogo com "j"
            self._start_game()

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

        if not self.bad_dogs:
            # Destroi os projeteis existentes e cria a nova frota
            self.bullets.empty()
            self._create_pack()
            self.settings.increase_speed()

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
        # Desenha o botão Jogar na tela se o jogo estiver inativo
        if not self.game_active:
            self.play_button.draw_button()
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

        # Detecta colisão entre bad_dog e o beagle
        if pygame.sprite.spritecollideany(self.beagle,self.bad_dogs):
            self._beagle_bited()
        
        # Procura por bad_dogs chegando a parte inferior da tela
        self._check_bad_dogs_bottom()

    def _check_bad_pack_edges(self):
        """ Responde apropriadamente se algum bad_dog chegou na borda da tela """
        for bad_dog in self.bad_dogs.sprites():
            if bad_dog.check_edges():
                self._change_bad_pack_direction()
                break
    
    def _change_bad_pack_direction(self):
        """ Faz toda a matilha descer e mudar de direção """
        for bad_dog in self.bad_dogs.sprites():
            bad_dog.rect.y += self.settings.bad_pack_drop_speed
        self.settings.bad_pack_direction *= -1

    def _beagle_bited(self):
        """ Responde ao Beagle sendo atacado pelos bad dogs """
        
        if self.stats.beagles_left > 0:
            # Decrementa o numero de vidas do Beagle (beagles_left)
            self.stats.beagles_left -= 1

            # Limpa os bad dogs e as balas restantes
            self.bullets.empty()
            self.bad_dogs.empty()

            # Cria uma nova matilha de bad dogs e centraliza o beagle
            self._create_pack()
            self.beagle.center_beagle()

            # Pausa rapida para reiniciar
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_bad_dogs_bottom(self):
        """ Verifica se algum bad_dog chegou até a parte inferior da tela """
        for bad_dog in self.bad_dogs.sprites():
            if bad_dog.rect.bottom >= self.settings.screen_height:
                # Trata isso como se o bad_dog tivesse mordido o Beagle
                self._beagle_bited()
                break
    
    def _check_play_button(self, mouse_pos):
        """ Inicia o jogo novo quando o jogador clica em Jogar """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Redefine as  configurações do jogo
            self.settings.initialize_dynamic_settings()
            # Zera as estatisticas do Jogo
            self._start_game()

            # Descarta qualquer projeteis e bad_dogs restantes
            self.bullets.empty()
            self.bad_dogs.empty()

            # Cria uma nova matilha e centraliza o Beagle
            self._create_pack()
            self.beagle.center_beagle()
    
    def _start_game(self):
        """ Inicializa o jogo e limpa as estatisticas """
        self.stats.reset_stats()
        self.game_active = True
        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)


if __name__ == '__main__':
    # Cria uma instancia do jogo e execute o jogo
    bb = BeagleBattle()
    bb.run_game()
