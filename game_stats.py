class GameStats:
    """ Rastreia as estatisticas: Uma Bigada a Beagle Battle """

    def __init__(self, bb_game):
        """ Inicializa as estatisticas """
        self.settings = bb_game.settings
        self.reset_stats()

    def reset_stats(self):
        """ Inicializa as estatisticas que podem mudar durante o jogo """
        self.beagles_left = self.settings.beagles_limit