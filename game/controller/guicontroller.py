from ..model.game import Game
from ..model.consoleplayer import ConsolePlayer
from ..model.aiplayer import AIPlayer
from .gamemode import GameMode
import random
import pygame
import time

class GUIController():

    def __init__(self, screen):
        self.screen = screen
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
        # while True:
        #     print('>>> ', end='', flush=True)
            
        #     if not self.gamemodel.is_game_over and isinstance(self.gamemodel.current_player, AIPlayer):
        #         self.make_ai_move()
        #         continue

        #     inp = input()    
        #     command = inp.split()[0]
        #     args = inp.split()[1:]
        #     if command == 'move':
        #         move = (int(args[0]), int(args[1]))
        #         self.gamemodel.move(*move)
        #     elif command == 'restart':
        #         gamemode = self.request_gamemode()
        #         players = self.create_players(gamemode)
        #         self.gamemodel.start(*players)
        #     elif command == 'exit':
        #         return
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    move = self.mouse_pos_to_move(pos)
                    self.gamemodel.move(*move)


    def mouse_pos_to_move(self, pos):
        w, h = pygame.display.get_surface().get_size()
        x = pos[0] - 0.2*w
        y = pos[1] - 0.2*h
        cell_diff = 0.6*w/8

        return (int(x/cell_diff)), (int(y/cell_diff))



    def make_ai_move(self):
        move = self.generate_move()
        time.sleep(1)
        print('move', *move)
        self.gamemodel.move(*move)

    def generate_move(self):
        moves = self.gamemodel.get_available_moves()
        move = random.choice(moves)
        return move