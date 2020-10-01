from .observer import Observer

class ConsoleView(Observer):
    def update(self, game):
        available_moves = game.get_available_moves()
        print(available_moves)
        print(game.current_player.name + " - ", game.current_player.get_point())
        print(game.another_player.name + " - ", game.another_player.get_point())
        for i in range(len(game.board)):
            for j in range(len(game.board)):
                if (i, j) in available_moves:
                    print("X", end = "")
                else:
                    out = 0
                    print(int(game.board[i][j]), end="")
            print()
        print()

    def game_over(self, game):
        if not is_None(game.winner):
            print(game.winner.name + " WIN")
        else:
            print("TIE")


