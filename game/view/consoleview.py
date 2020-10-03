from .observer import Observer
from ..model.gameevent import GameEvent

class ConsoleView(Observer):
    def update(self, game, event):
        if event == GameEvent.GAME_STARTED:
            print("==========[ Reversi ]==========")
            self.redraw(game)
        elif event == GameEvent.FIELD_UPDATED:
            self.redraw(game)
        elif event == GameEvent.NEXT_MOVE:
            self.notify_moving_player(game)
        elif event == GameEvent.PLAYER_PASSES:
            self.notify_passed_player(game)
        elif event == GameEvent.INCORRECT_MOVE:
            self.notify_incorrect_move(game)
        elif event == GameEvent.GAME_OVER:
            self.nofify_game_over(game)

        # print(game.current_player.name + " - ", game.current_player.get_point())
        # print(game.another_player.name + " - ", game.another_player.get_point())


    def nofify_game_over(self, game):
        if game.winner:
            print(game.winner.name + " WIN")
        else:
            print("TIE")
        print('Enter restart to continue or exit to leave.')

    def notify_passed_player(self, game):
        print('The', game.current_player.name, 'passes the turn.')

    def redraw(self, game):
        self.render_field(game)
        self.render_available_moves(game)

    def render_available_moves(self, game):
        print('List of available moves:', game.get_available_moves())

    def render_field(self, game):
        available_moves = game.get_available_moves()
        for i in range(len(game.board)):
            for j in range(len(game.board)):
                if (i, j) in available_moves:
                    print("X", end = " ")
                else:
                    out = 0
                    print(int(game.board[i][j]), end=" ")
            print()
        print()

    def notify_incorrect_move(self, game):
        print('Incorrect move, try again!')


    def notify_moving_player(self, game):
        print(game.current_player.name, ' your turn.')