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
        if event == GameEvent.GAME_STARTED:
            print("==========[ Reversi ]==========")
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

        # print(game.current_player.name + " - ", game.current_player.get_point())
        # print(game.another_player.name + " - ", game.another_player.get_point())


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
        self.render_field(game)

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