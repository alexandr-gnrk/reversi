from game.model.game import Game
from game.model.consoleplayer import ConsolePlayer
from game.view.consoleview import ConsoleView
from game.controller.consolecontroller import ConsoleController


controller = ConsoleController()
view = ConsoleView()
controller.gamemodel.attach(view)

controller.start()