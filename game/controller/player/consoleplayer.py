from abc import abstractmethod
import random
import time

from .player import Player


class ConsolePlayer(Player):
    def __init__(self, name):
        super(ConsolePlayer, self).__init__(name)

    @abstractmethod
    def get_command(self):
        pass


class HumanPlayer(ConsolePlayer):
    def __init__(self, name):
        super(HumanPlayer, self).__init__(name)

    def get_move(self, _):
        args = input().split()
        move = (int(args[0]), int(args[1]))
        return move

    def get_command(self):
        return input().strip()


class AIPlayer(ConsolePlayer):
    def __init__(self, name):
        super(AIPlayer, self).__init__(name)

    def get_move(self, model):
        # get list of available movements and choose random
        moves = model.get_available_moves()
        move = random.choice(moves)
        # imitate thinking of AI
        time.sleep(1)
        # type AI movement to console (for user view)
        print(*move)
        return move

    def get_command(self):
        # AI always choose to move
        command = 'move'
        print(command)
        return command