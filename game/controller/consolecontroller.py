from ..model.game import Game
from ..model.consoleplayer import ConsolePlayer
from ..model.aiplayer import AIPlayer
from .gamemode import GameMode
import random
import time

class ConsoleController():

    def __init__(self):
        gamemode = self.request_gamemode()

        player1 = ConsolePlayer('Player1')
        if gamemode == GameMode.PLAYER_VS_PLAYER:
            player2 = ConsolePlayer('Player2')
        else:
            player2 = AIPlayer('Player2')

        self.gamemodel = Game(player1, player2)
    

    def request_gamemode(self):
        mode = int(input('Enter game mode (0 - Player vs Player, 1 - Player vs Bot): '))
        if mode == 0:
            return GameMode.PLAYER_VS_PLAYER
        else:
            return GameMode.PLAYER_VS_BOT


    def start(self):
        print('======[ Reversi ]======')
        while True:
            if isinstance(self.gamemodel.current_player, ConsolePlayer):
                move = self.request_move_from_console()
            else:
                move = self.generate_move()
            self.gamemodel.move(*move)

    def request_move_from_console(self):
        move_str = input(self.gamemodel.current_player.name + ' move: ')
        return list(map(int, move_str.split()))

    def generate_move(self):
        move_str = print(self.gamemodel.current_player.name + ' move:  ', end='', flush=True)
        moves = self.gamemodel.get_available_moves()
        move = random.choice(moves)
        time.sleep(random.randint(1, 5))
        print(*move)
        return move