import itertools
from .cell import Cell
from .subject import Subject

class Game(Subject):

    def __init__(self, player1, player2, dimension=8):
        self.board = list()
        self.current_player = player1
        self.another_player = player2
        self.current_player.color = Cell.BLACK
        self.another_player.color = Cell.WHITE
        self.winner = None
        
        self.observers = list()

        self.initial_placement(dimension)

        
    def attach(self, observer):
        self.observers.append(observer)
        self.notify()



    def detach(self, observer):
        self.observers.remove(observer)


    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def notify_end(self):
        for observer in self.observers:
            observer.game_over(self)


    def initial_placement(self, dimension):
        for i in range(dimension):
            self.board.append([Cell.EMPTY] * dimension)
        self.board[dimension // 2 - 1][dimension // 2 - 1] = Cell.WHITE
        self.board[dimension // 2 - 1][dimension // 2] = Cell.BLACK
        self.board[dimension // 2][dimension // 2 - 1] = Cell.BLACK
        self.board[dimension // 2][dimension // 2] = Cell.WHITE


    def change_player(self):
        self.current_player, self.another_player = self.another_player, self.current_player


    def get_available_moves(self):
        available_moves = list()
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.is_available_cell(i, j):
                    available_moves.append((i, j))
        return available_moves


    def is_available_cell(self, i, j):
        if self.board[i][j] != Cell.EMPTY:
            return False

        for diff in itertools.product([-1, 0, 1], repeat=2):
            i_diff, j_diff = diff
            if self.is_line_bounded(i, j, i_diff, j_diff):
                return True

        return False


    def is_cell_exist(self, i, j):
        if i >= 0 and j >= 0 and i < len(self.board) and j < len(self.board):
            return True
        return False


    def is_line_bounded(self, i, j, i_diff, j_diff):
        i += i_diff
        j += j_diff
        amount = 0
        while self.is_cell_exist(i, j) and (self.board[i][j] == self.another_player.color):
            i += i_diff
            j += j_diff
            amount += 1
        if self.is_cell_exist(i, j) and (self.board[i][j] == self.current_player.color) and (amount > 0):
            return True

        return False


    def reverse_line(self, i, j, i_diff, j_diff):
        i += i_diff
        j += j_diff
        while (self.board[i][j] == self.another_player.color):
            self.reverse_cell(i, j)
            i += i_diff
            j += j_diff


    def reverse_cell(self, i, j):
        self.board[i][j] = self.current_player.color
        self.current_player.inc_point()
        self.another_player.dec_point()


    def update_lines(self, i, j):
        for diff in itertools.product([-1, 0, 1], repeat=2):
            i_diff, j_diff = diff
            if self.is_line_bounded(i, j, i_diff, j_diff):
                self.reverse_line(i, j, i_diff, j_diff)

    
    def move(self, i, j):
        self.update_lines(i, j)
        self.board[i][j] = self.current_player.color
        self.current_player.inc_point()
        self.change_player()
        self.notify()
        if not self.get_available_moves():
            self.change_player()
            #notify PASS            
        self.check_end_game()


    def check_end_game(self):
        if not self.get_available_moves():
            self.end_game()
            
    def end_game(self):
        if self.current_player.get_point() > self.another_player.get_point():
            self.winner = self.current_player
        elif self.current_player.get_point() < self.another_player.get_point():
            self.winner = self.another_player

        self.notify_end()
