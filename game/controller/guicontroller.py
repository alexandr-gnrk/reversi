import pygame
import queue
import threading

from ..model.game import Game
from .player.guiplayer import HumanPlayer, AIPlayer
from .gamemode import GameMode


class GUIController():

    def __init__(self, screen, experimental=False):
        self.gamemode = None
        self.screen = screen
        self.gamemodel = Game()
        self.is_exit = False
        self.experimental = experimental
        self.tracking = None
        self.movement = queue.Queue(1)


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


    def start(self):
        # init gamemodel by default gamemode
        self.gamemode = GameMode.PLAYER_VS_PLAYER
        players = self.create_players(self.gamemode)
        self.gamemodel.start(*players)

        self.reset_tracking()
        # game loop
        while not self.is_exit:
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
            
            # check is present move in queue
            if not self.movement.empty():
                self.gamemodel.move(*self.movement.get())
                self.reset_tracking()

            for event in pygame.event.get(pygame.QUIT):
                self.exit()

        pygame.quit()


    def reset_tracking(self):
        # make thread that track mouse movents, and add movement to the queue
        # when button pressed on the field
        target = self.gamemodel.current_player.get_move
        self.tracking = threading.Thread(target=target, args=(self.movement, self.gamemodel))
        self.tracking.start()


    def change_gamemode(self, gamemode):
        # change gamemode and restart game
        self.gamemode = gamemode
        self.restart()


    def exit(self):
        self.is_exit = True


    def restart(self):
        players = self.create_players(self.gamemode)
        self.gamemodel.start(*players)
        self.reset_tracking()


    def button(self, msg, x, y, w, h, action=None):
        # get mouse position and mouse pressed information
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # check is mouse inside button box
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            if click[0] == 1 and action != None:
                action()