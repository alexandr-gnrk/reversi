import pygame

from game.model.game import Game
from game.model.consoleplayer import ConsolePlayer
from game.view.consoleview import ConsoleView
from game.view.guiview import GUIView
from game.controller.consolecontroller import ConsoleController
from game.controller.guicontroller import GUIController




pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Reversi')
icon = pygame.image.load('./src/logo.png')
pygame.display.set_icon(icon)

controller = GUIController(screen)
view = ConsoleView()
view1 = GUIView(screen)
controller.gamemodel.attach(view)
controller.gamemodel.attach(view1)
controller.start()