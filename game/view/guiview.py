import pygame
from .observer import Observer
from ..model.gameevent import GameEvent
from ..model.cell import Cell


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
WHITE_GREEN = (0, 138, 0)
BLACK_GREEN = (0, 130, 0)
BLACK_GREEN1 = (0, 114, 0)
BLACK_RED = (128, 0, 0)


class GUIView(Observer):

    def __init__(self, screen):
        self.screen = screen

    def update(self, game, event):
        self.game = game
        if event == GameEvent.GAME_STARTED:
            self.redraw(game)
        elif event == GameEvent.FIELD_UPDATED:
            self.redraw(game)
        elif event == GameEvent.NEXT_MOVE:
            self.notify_moving_player(game)
        elif event == GameEvent.PLAYER_PASSES:
            self.notify_passed_player(game)
        elif event == GameEvent.INCORRECT_MOVE:
            self.notify_incorrect_move(game)
        elif event == GameEvent.GAME_OVER:
            self.nofify_game_over(game)


    def nofify_game_over(self, game):
        if game.winner:
            text = game.winner.name + ' wins!'
        else:
            text = 'Tie!'
        w, h = pygame.display.get_surface().get_size()
        TextSurf, TextRect = self.text_objects(text, 25, BLACK_RED)
        TextRect.center = ((w / 2),(h * 0.1))
        self.screen.blit(TextSurf, TextRect)
        pygame.display.update()


    def notify_passed_player(self, game):
        w, h = pygame.display.get_surface().get_size()
        TextSurf, TextRect = self.text_objects('The ' + game.current_player.name + ' passes the turn.')
        TextRect.center = ((w / 2),(h * 0.9))
        self.screen.blit(TextSurf, TextRect)
        pygame.display.update()


    def redraw(self, game):
        if self.game.current_player.name == 'Player1':
            player1 = self.game.current_player
            player2 = self.game.another_player
        else:
            player1 = self.game.another_player
            player2 = self.game.current_player

        self.render_field(game)

        w, h = pygame.display.get_surface().get_size()
        TextSurf, TextRect = self.text_objects('Player1: ' + str(player1.get_point()))
        TextRect.center = (0.1*w, (h * 0.5))
        self.screen.blit(TextSurf, TextRect)
        
        TextSurf, TextRect = self.text_objects('Player2: ' + str(player2.get_point()))
        TextRect.center = ((0.9*w),(h * 0.5))
        self.screen.blit(TextSurf, TextRect)

        self.button('Restart', 25, 525, 100, 50, (241,241,241), (255,241,241))
        self.button('Exit', 475, 525, 100, 50, (241,241,241), (255,241,241))
        self.button('Player vs Player', 25, 20, 100, 25, (241,241,241), (255,241,241))
        self.button('Player vs Bot', 25, 55, 100, 25, (241,241,241), (255,241,241))
        # self.button('Bot vs Bot', 25, 90, 100, 25, (241,241,241), (255,241,241))
        pygame.display.update() 


    def render_field(self, game):
        self.screen.fill((0, 160, 0))
        self.draw_field()
        self.draw_chips(game)
        pygame.display.update()


    def text_objects(self, text, font_size=18, color=BLACK):
        font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()


    def notify_incorrect_move(self, game):
        w, h = pygame.display.get_surface().get_size()
        TextSurf, TextRect = self.text_objects('Incorrect move, try again!')
        TextRect.center = ((w / 2),(h * 0.1))
        self.screen.blit(TextSurf, TextRect)
        pygame.display.update()


    def notify_moving_player(self, game):
        w, h = pygame.display.get_surface().get_size()
        TextSurf, TextRect = self.text_objects(game.current_player.name + ' your turn.')
        TextRect.center = ((w / 2),(h * 0.9))
        self.screen.blit(TextSurf, TextRect)
        pygame.display.update()


    def draw_field(self):
        w, h = pygame.display.get_surface().get_size()
        left, top = 0.2*w, 0.2*h
        width, height = 0.6*w, 0.6*h
        cell_diff = width / 8

        for i in range(8):
            rleft = left + i*cell_diff
            for j in range(8):
                rtop = top + j*cell_diff
                if (i + j) % 2 == 0:
                    color = WHITE_GREEN
                else:
                    color = BLACK_GREEN
                pygame.draw.rect(self.screen, color, (rleft, rtop, cell_diff, cell_diff))

        for i in range(1, 8):
            cur_diff = i*cell_diff

            start_pos = (top, left + cur_diff)
            end_pos = (top + height, left + cur_diff)
            pygame.draw.line(self.screen, BLACK, start_pos, end_pos)

            start_pos = (left  + cur_diff, top)
            end_pos = (left + cur_diff, top + height)
            pygame.draw.line(self.screen, BLACK, start_pos, end_pos)


    def draw_chips(self, game):
        w, h = pygame.display.get_surface().get_size()
        left, top = 0.2*w, 0.2*h
        width, height = 0.6*w, 0.6*h
        cell_diff = width / 8

        available_moves = game.get_available_moves()
        for i in range(len(game.board)):
            rleft = left + i*cell_diff
            for j in range(len(game.board)):
                rtop = top + j*cell_diff
                center = (rleft + cell_diff/2, rtop + cell_diff/2)
                
                if (i, j) in available_moves:
                    color = BLACK_GREEN1
                elif game.board[i][j] == Cell.EMPTY:
                    continue
                elif game.board[i][j] == Cell.BLACK:
                    color = BLACK
                elif game.board[i][j] == Cell.WHITE:
                    color = WHITE                

                pygame.draw.circle(self.screen,
                    color, center, cell_diff/2*0.8)


    def button(self, msg, x, y, w, h, ic, ac):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.screen, ac,(x,y,w,h))
        else:
            pygame.draw.rect(self.screen, ic,(x,y,w,h))

        font = pygame.font.Font(pygame.font.get_default_font(), 12)
        textSurf = font.render(msg, True, (0,0,0))
        textRect = textSurf.get_rect()

        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.screen.blit(textSurf, textRect)