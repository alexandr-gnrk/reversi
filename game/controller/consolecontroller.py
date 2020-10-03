from ..model.game import Game
from ..model.consoleplayer import ConsolePlayer
from ..model.aiplayer import AIPlayer
from .gamemode import GameMode
import random
import time

class ConsoleController():

    def __init__(self):
        self.gamemodel = Game()

    def create_players(self, gamemode):
        if gamemode == GameMode.PLAYER_VS_PLAYER:
            player1 = ConsolePlayer('Player1')
            player2 = ConsolePlayer('Player2')
        elif gamemode == GameMode.PLAYER_VS_BOT:
            player1 = ConsolePlayer('Player1')
            player2 = AIPlayer('Player2')
        else:
            player1 = AIPlayer('Player1')
            player2 = AIPlayer('Player2')

        return player1, player2


    def request_gamemode(self):
        print('Game mods:')
        print('    0 - Player vs Player')
        print('    1 - Player vs Bot')
        print('    2 - Bot vs Bot')
        mode = int(input('Enter game mode: '))
        if mode == 0:
            return GameMode.PLAYER_VS_PLAYER
        elif mode == 1:
            return GameMode.PLAYER_VS_BOT
        else:
            return GameMode.BOT_VS_BOT


    def start(self):
        gamemode = self.request_gamemode()
        players = self.create_players(gamemode)
        self.gamemodel.start(*players)
        while True:
            print('>>> ', end='', flush=True)
            
            if not self.gamemodel.is_game_over and isinstance(self.gamemodel.current_player, AIPlayer):
                self.make_ai_move()
                continue

            inp = input()    
            command = inp.split()[0]
            args = inp.split()[1:]
            if command == 'move':
                move = (int(args[0]), int(args[1]))
                self.gamemodel.move(*move)
            elif command == 'restart':
                gamemode = self.request_gamemode()
                players = self.create_players(gamemode)
                self.gamemodel.start(*players)
            elif command == 'exit':
                return

    def make_move(self):
        if isinstance(self.gamemodel.current_player, ConsolePlayer):
            move = self.get_move_from_console()
        else:
            move = self.generate_move()
        self.gamemodel.move(*move)

    def make_ai_move(self):
        move = self.generate_move()
        time.sleep(1)
        print('move', *move)
        self.gamemodel.move(*move)

    def generate_move(self):
        moves = self.gamemodel.get_available_moves()
        move = random.choice(moves)
        return move