from .observer import Observer

class ConsoleView(Observer):
    def update(self, game):
        available_moves = game.get_available_moves()
        print(available_moves)
        for i in range(len(game.board)):
            for j in range(len(game.board)):
                if (i, j) in available_moves:
                    print("X", end = "")
                else:
                    out = 0
                    print(int(game.board[i][j]), end="")
            print()
        print()
