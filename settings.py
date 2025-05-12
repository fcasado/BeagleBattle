class Settings:
    """ Classe para armazenar as configurações do jogo Uma Bigada """

    def __init__(self):
        """ Inicializa as configurações do jogo """
        # Configurações de tela
        self.screen_width = 1300
        self.screen_height = 900
        self.bg_color = (255,255,255)

        # Configurações do beagle
        self.beagle_speed = 3.5

        # Configurações da bala (osso)
        self.bullet_speed = 7.0
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (150, 75, 0)

        # Configurações de cadencia de tiro
        self.bullets_allowed = 10

        # Configurações dos malvadões (Bad Dogs)
        self.bad_speed = 1.0
        self.bad_pack_drop_speed = 10

        # Direção dos malvadões 1 = direita, -1 = esquerda (Bad Dogs)
        self.bad_pack_direction = 1
        
