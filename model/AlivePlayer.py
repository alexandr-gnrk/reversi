from Player import Player


class AlivePlayer(Player):
    def __init__(self, name):
        Player.__init__(self)
        self.name = name

    def make_move(self, available_moves, move):
        if move in available_moves > 0:
            return move
