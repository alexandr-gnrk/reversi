from ..model.game import Game
from ..model.antigame import AntiGame
from .player.consoleplayer import HumanPlayer, AIPlayer
from .gamemode import GameMode
import random
import time


class ConsoleController():

    def __init__(self, black_hole=None, experimental=False):
        # set Anti-Reversi mode if black hole was passed
        if black_hole:
            self.gamemodel = AntiGame(black_hole)
        else:
            self.gamemodel = Game()
        self.experimental = experimental


    def create_players(self, gamemode):
        # create players depends on game mode
        if gamemode == GameMode.PLAYER_VS_PLAYER:
            player1 = HumanPlayer('Player1')
            player2 = HumanPlayer('Player2')
        elif gamemode == GameMode.PLAYER_VS_BOT:
            player1 = HumanPlayer('Player1')
            player2 = AIPlayer('Player2')
        else:
            player1 = AIPlayer('Player1')
            player2 = AIPlayer('Player2')

        return player1, player2


    def request_gamemode(self):
        print('Game mods:')
        print('    0 - Player vs Player')
        print('    1 - Player vs Bot')
        if self.experimental:
            print('    2 - Bot vs Bot')

        # prompt for input gamemode
        mode = int(input('Enter game mode: '))
        if mode == 0:
            return GameMode.PLAYER_VS_PLAYER
        elif mode == 1:
            return GameMode.PLAYER_VS_BOT
        else:
            # by default return Bot vs Bot mode
            return GameMode.BOT_VS_BOT


    def start(self):
        # get parametrs from conslon and create game model 
        gamemode = self.request_gamemode()
        players = self.create_players(gamemode)
        self.gamemodel.start(*players)

        # game loop
        while True:
            # show prompt for input 
            print('Command: ', end='', flush=True)

            # get input and extract command and args
            command = self.gamemodel.current_player.get_command()

            # make action that depends on command
            if command == 'move':
                print('Enter pos: ', end='', flush=True)
                move = self.gamemodel.current_player.get_move(self.gamemodel)
                self.gamemodel.move(*move)
            elif command == 'restart':
                gamemode = self.request_gamemode()
                players = self.create_players(gamemode)
                self.gamemodel.start(*players)
            elif command == 'exit':
                return
            else:
                print('Try again!')