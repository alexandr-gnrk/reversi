from ..model.game import Game
from ..model.consoleplayer import ConsolePlayer
from ..model.aiplayer import AIPlayer
from .gamemode import GameMode
import random
import pygame
import time


class GUIController():

    def __init__(self, screen, experimental=False):
        self.gamemode = None
        self.screen = screen
        self.gamemodel = Game()
        self.is_exit = False
        self.experimental = experimental


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


    def start(self):
        # init gamemodel by default gamemode
        self.gamemode = GameMode.PLAYER_VS_PLAYER
        players = self.create_players(self.gamemode)
        self.gamemodel.start(*players)

        # game loop
        while True:
            # check is buttons were pressed and make corresponding action
            self.button('Restart', 25, 525, 100, 50, 
                action=self.restart)
            self.button('Exit', 475, 525, 100, 50, 
                action=self.exit)
            self.button('Player vs Player', 25, 20, 100, 25, 
                action=lambda: self.change_gamemode(GameMode.PLAYER_VS_PLAYER))
            self.button('Player vs Bot', 25, 55, 100, 25, 
                action=lambda: self.change_gamemode(GameMode.PLAYER_VS_BOT))
            if self.experimental:
                self.button('Bot vs Bot', 25, 90, 100, 25, 
                    action=lambda: self.change_gamemode(GameMode.BOT_VS_BOT))

            if self.is_exit:
                return
            
            # if it's AI player then make move
            if not self.gamemodel.is_game_over and \
                    isinstance(self.gamemodel.current_player, AIPlayer):
                self.make_ai_move()
            
            # events handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEBUTTONUP:
                    # get mouse position and translate it to
                    # game coordinate grid
                    pos = pygame.mouse.get_pos()
                    move = self.mouse_pos_to_move(pos)
                    # chek is mouse on game field and make move
                    if (0 <= move[0] <= 7) and (0 <= move[1] <= 7):
                        self.gamemodel.move(*move)


    def change_gamemode(self, gamemode):
        # change gamemode and restart game
        self.gamemode = gamemode
        self.restart()


    def restart(self):
        # restart game
        players = self.create_players(self.gamemode)
        self.gamemodel.start(*players)


    def exit(self):
        self.is_exit = True


    def mouse_pos_to_move(self, pos):
        # get distplay properites
        w, h = pygame.display.get_surface().get_size()
        # offset position to start of
        # game field
        x = pos[0] - 0.2*w
        y = pos[1] - 0.2*h
        # get single cell size on field
        cell_diff = 0.6*w/8
        # translate x, y to integer coordinates on the field 
        i = x//cell_diff
        j = y//cell_diff
        return int(i), int(j)


    def button(self, msg, x, y, w, h, action=None):
        # get mouse position and mouse pressed information
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # check is mouse inside button box
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            if click[0] == 1 and action != None:
                action()


    def make_ai_move(self):
        move = self.generate_move()
        # imitate thinking of AI
        time.sleep(1)
        # and make movement
        self.gamemodel.move(*move)


    def generate_move(self):
        # get list of available movements and choose random
        moves = self.gamemodel.get_available_moves()
        move = random.choice(moves)
        return move