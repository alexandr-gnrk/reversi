from model.game import Game
from model.consoleplayer import ConsolePlayer
from view.consoleview import ConsoleView


view = ConsoleView()
g = Game(ConsolePlayer('Sasha'), ConsolePlayer('Vanya'))
g.attach(view)
