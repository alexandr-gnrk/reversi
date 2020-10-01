from game import Game
from consoleplayer import ConsolePlayer


g = Game(ConsolePlayer('Sasha'), ConsolePlayer('Vanya'))
g.print_board()
