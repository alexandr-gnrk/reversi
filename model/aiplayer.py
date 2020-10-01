from .player import Player


class AIPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)