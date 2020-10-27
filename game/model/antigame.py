from .game import Game
from .cell import Cell


class AntiGame(Game):
    """Realization of Anti-Reversi with black hole"""
    def __init__(self, hole_pos):
        super().__init__()
        self.hole_pos = hole_pos

    def initial_placement(self, dimension):
        super().initial_placement(dimension)
        hole_x, hole_y = self.hole_pos
        self.board[hole_x][hole_y] = Cell.HOLE

    def is_available_cell(self, i, j):
        return self.board[i][j] != Cell.HOLE and \
            super().is_available_cell(i, j)

    def is_cell_exist(self, i, j):
        return super().is_cell_exist(i, j) and \
            self.board[i][j] != Cell.HOLE
            
