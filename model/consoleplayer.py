from .player import Player

class ConsolePlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)