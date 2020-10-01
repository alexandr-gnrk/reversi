DEFULT_DIMENSION = 8


class Game:
    def __init__(self, player1, player2):
        self.dimension = DEFULT_DIMENSION
        self.initial_placement(player1, player2)

    # def __init__(self, d, player1, player2):
    #     self.dimension = d if d > 2 and d % 2 != 0 else DEFULT_DIMENSION
    #     self.initial_placement(player1, player2)

    def initial_placement(self, player1, player2):
        self.board = []
        for i in range(self.dimension):
            self.board.append([0] * self.dimension)
        self.board[self.dimension // 2 - 1][self.dimension // 2 - 1] = 1
        self.board[self.dimension // 2 - 1][self.dimension // 2] = -1
        self.board[self.dimension // 2][self.dimension // 2 - 1] = -1
        self.board[self.dimension // 2][self.dimension // 2] = 1

        self.player1 = player1
        self.player2 = player2

        self.current_player = player1
        self.another_player = player2

        self.current_player.color = -1
        self.another_player.color = 1

        self.passes = 0

    def change_player(self):
        self.current_player, self.another_player = self.another_player, self.current_player

    def get_available_moves(self):
        available_moves = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0 and self.is_available_cell(i, j):
                    available_moves.append((i, j))
        return available_moves

    def is_available_cell(self, i, j):
        is_available = False
        for change_i in [-1, 0, 1]:
            for change_j in [-1, 0, 1]:
                is_available = is_available or self.check_line(
                    i, j, change_i, change_j)
        return is_available

    def check_line(self, i, j, change_i, change_j):
        i += change_i
        j += change_j
        count = 0
        while (i >= 0) and (j >= 0) and (i < self.dimension) and (j < self.dimension) and (self.board[i][j] == self.another_player.color):
            i += change_i
            j += change_j
            count += 1
        if (i >= 0) and (j >= 0) and (i < self.dimension) and (j < self.dimension) and (self.board[i][j] == self.current_player.color) and (count > 0):
            return True

        return False

    def reverse_line(self, i, j, change_i, change_j):
        i += change_i
        j += change_j
        while (self.board[i][j] == self.another_player.color):
            self.reverse_cell(i, j)
            i += change_i
            j += change_j

    def reverse_cell(self, i, j):
        self.board[i][j] = self.current_player.color
        self.current_player.inc_point()
        self.another_player.dec_point()

    def move(self, i, j):
        for change_i in [-1, 0, 1]:
            for change_j in [-1, 0, 1]:
                if self.check_line(i, j, change_i, change_j):
                    self.reverse_line(i, j, change_i, change_j)

        self.board[i][j] = self.current_player.color
        self.current_player.inc_point()
        self.change_player()

    def print_board(self):
        available_moves = self.get_available_moves()
        for i in range(self.dimension):
            for j in range(self.dimension):
                if (i, j) in available_moves:
                    print("X", end = "")
                else:
                    print(2 if self.board[i][j] == -1
                          else self.board[i][j], end="")
            print()
        print()
