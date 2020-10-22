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
        # create players depends on game mode
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
        # print('    2 - Bot vs Bot')

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
            print('>>> ', end='', flush=True)
            
            # if it's AI player then make move
            if not self.gamemodel.is_game_over and \
                    isinstance(self.gamemodel.current_player, AIPlayer):
                self.make_ai_move()
                continue

            # get input and extract command and args
            inp = input()    
            command = inp.split()[0]
            args = inp.split()[1:]

            # make action that depends on command
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
        # get move coordinates and make movement
        move = self.get_move_from_console()
        self.gamemodel.move(*move)


    def make_ai_move(self):
        move = self.generate_move()
        # imitate thinking of AI
        time.sleep(1)
        # type AI movement to console (for user view)
        print('move', *move)
        self.gamemodel.move(*move)


    def generate_move(self):
        # get list of available movements and choose random
        moves = self.gamemodel.get_available_moves()
        move = random.choice(moves)
        return move