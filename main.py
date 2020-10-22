import argparse


parser = argparse.ArgumentParser(
    description="Reversi game with Othello rule-set")
parser.add_argument(
    '-m', '--mode', 
    choices=('gui', 'console'),
    default='gui',
    dest='mode',
    help='game mode')
parser.add_argument(
    '-e', '--experimental',
    action='store_true',
    dest='experimental',
    help='enable experimental features')

args = parser.parse_args()

if args.mode == 'gui':
    import pygame
    from game.view.guiview import GUIView
    from game.controller.guicontroller import GUIController

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Reversi')
    icon = pygame.image.load('./src/logo.png')
    pygame.display.set_icon(icon)

    controller = GUIController(screen, args.experimental)
    view = GUIView(screen, args.experimental)
    controller.gamemodel.attach(view)
    controller.start()
else:
    from game.view.consoleview import ConsoleView
    from game.controller.consolecontroller import ConsoleController

    controller = ConsoleController(args.experimental)
    view = ConsoleView()
    controller.gamemodel.attach(view)
    controller.start()