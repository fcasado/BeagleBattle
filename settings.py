class Settings:
    """ Classe para armazenar as configurações do jogo Uma Bigada """

    def __init__(self):
        """ Inicializa as configurações do jogo """
        # Configurações de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)

        # Configurações do beagle
        self.beagle_speed = 3.5

        # Configurações da bala (osso)
        self.bullet_speed = 7.0
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (150, 75, 0)