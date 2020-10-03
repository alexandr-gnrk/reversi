from ..model.game import Game
from ..model.consoleplayer import ConsolePlayer
from ..model.aiplayer import AIPlayer
from .gamemode import GameMode
import random
import pygame
import time

class GUIController():

    def __init__(self, screen):
        self.gamemode = GameMode.PLAYER_VS_PLAYER
        self.screen = screen
        self.gamemodel = Game()
        self.is_end = False


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


    def start(self):
        # gamemode = self.request_gamemode()
        gamemode = GameMode.PLAYER_VS_PLAYER
        players = self.create_players(gamemode)
        self.gamemodel.start(*players)

        while True:
            self.button('Restart', 25, 525, 100, 50, action=self.restart)
            self.button('Exit', 475, 525, 100, 50, action=self.exit)
            self.button('Player vs Player', 25, 20, 100, 25, action=self.player_vs_player)
            self.button('Player vs Bot', 25, 55, 100, 25, action=self.player_vs_bot)
            # self.button('Bot vs Bot', 25, 90, 100, 25, action=self.bot_vs_bot)

            if self.is_end:
                return
            
            if not self.gamemodel.is_game_over and isinstance(self.gamemodel.current_player, AIPlayer):
                self.make_ai_move()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    move = self.mouse_pos_to_move(pos)
                    if (0 <= move[0] <= 7) and (0 <= move[1] <= 7):
                        self.gamemodel.move(*move)


    def player_vs_player(self):
        self.gamemode = GameMode.PLAYER_VS_PLAYER
        players = self.create_players(self.gamemode)
        self.gamemodel.start(*players)
        self.is_end = False


    def player_vs_bot(self):
        self.gamemode = GameMode.PLAYER_VS_BOT
        players = self.create_players(self.gamemode)
        self.gamemodel.start(*players)
        self.is_end = False


    def bot_vs_bot(self):
        self.gamemode = GameMode.BOT_VS_BOT
        players = self.create_players(self.gamemode)
        self.gamemodel.start(*players)
        self.is_end = False


    def restart(self):
        gamemode = self.gamemode
        players = self.create_players(gamemode)
        self.gamemodel.start(*players)


    def exit(self):
        self.is_end = True


    def mouse_pos_to_move(self, pos):
        w, h = pygame.display.get_surface().get_size()
        x = pos[0] - 0.2*w
        y = pos[1] - 0.2*h
        cell_diff = 0.6*w/8

        return (int(x/cell_diff)), (int(y/cell_diff))


    def button(self, msg, x, y, w, h, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            if click[0] == 1 and action != None:
                action()


    def make_ai_move(self):
        move = self.generate_move()
        time.sleep(1)
        self.gamemodel.move(*move)


    def generate_move(self):
        moves = self.gamemodel.get_available_moves()
        move = random.choice(moves)
        return move