class Settings:
    """ Classe para armazenar as configurações do jogo Uma Bigada """

    def __init__(self):
        """ Inicializa as configurações do jogo """
        # Configurações de tela
        self.screen_width = 1300
        self.screen_height = 900
        self.bg_color = (255,255,255)

        # Configurações do beagle
        #self.beagle_speed = 3.5
        self.beagles_limit = 2

        # Configurações da bala (osso)
        #self.bullet_speed = 7.0
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (150, 75, 0)
        # Configurações de cadencia de tiro
        self.bullets_allowed = 10

        # Configurações dos malvadões (Bad Dogs)
        #self.bad_speed = 8.0
        self.bad_pack_drop_speed = 10

        # Direção dos malvadões 1 = direita, -1 = esquerda (Bad Dogs)
        #self.bad_pack_direction = 1

        # A rapidez com que o jogo acelera
        self.speedup_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """ Inicializa as configurações que mudam a dificuldade do jogo """
        self.beagle_speed = 1.5
        self.bullet_speed = 2.5
        self.bad_speed = 1.0
        # Direção dos malvadões 1 = direita, -1 = esquerda (Bad Dogs)
        self.bad_pack_direction = 1

    def increase_speed(self):
        """ Aumenta as configurações de velocidade """
        self.beagle_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.bad_speed *= self.speedup_scale