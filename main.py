from game.model.game import Game
from game.model.consoleplayer import ConsolePlayer
from game.view.consoleview import ConsoleView
from game.controller import consolecontroller

view = ConsoleView()
g = Game(ConsolePlayer('Sasha'), ConsolePlayer('Vanya'))
g.attach(view)
