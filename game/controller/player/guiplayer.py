import pygame
import random
import time
from abc import abstractmethod
from .player import Player


class GUIPlayer(Player):
    def __init__(self, name):
        super(GUIPlayer, self).__init__(name)


class HumanPlayer(GUIPlayer):
    def __init__(self, name):
        super(HumanPlayer, self).__init__(name)

    def get_move(self, movement, _):
        # check is pygame is initialized
        while pygame.get_init() and movement.empty():
            for event in pygame.event.get(pygame.MOUSEBUTTONUP):
                # get mouse position and translate it to
                # game coordinate grid
                pos = pygame.mouse.get_pos()
                move = self.__mouse_pos_to_move(pos)
                # chek is mouse on game field and make move
                if (0 <= move[0] <= 7) and (0 <= move[1] <= 7):
                    movement.put(move)
                    return

    def __mouse_pos_to_move(self, pos):
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


class AIPlayer(GUIPlayer):
    def __init__(self, name):
        super(AIPlayer, self).__init__(name)

    def get_move(self, movement, model):
        # get list of available movements and choose random
        moves = model.get_available_moves()
        move = random.choice(moves)        
        # imitate thinking of AI
        time.sleep(1)
        # and put movement
        movement.put(move)
