import pygame
from .observer import Observer
from ..model.gameevent import GameEvent
from ..model.cell import Cell


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
WHITE_GREEN = (0, 138, 0)
BLACK_GREEN = (0, 120, 0)
BLACK_GREEN1 = (0, 100, 5)
BLACK_RED = (128, 0, 0)
BUTTON = (241, 241, 241)
BUTTON_HOVER = (189, 189, 189)


class GUIView(Observer):

    def __init__(self, screen):
        self.screen = screen
        self.w, self.h = pygame.display.get_surface().get_size()

    def update(self, game, event):
        self.game = game
        if event == GameEvent.GAME_STARTED:
            self.redraw(game)
            self.notify_moving_player(game)
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
        pygame.display.update()


    def render_text(self, text, dest, color=BLACK, font_size=18):
        # select font
        font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        # render text
        surface = font.render(text, True, color)
        # define the center
        left = dest[0] - surface.get_width() // 2
        top = dest[1] - surface.get_height() // 2
        self.screen.blit(surface, (left, top))


    def nofify_game_over(self, game):
        if game.winner:
            text = game.winner.name + ' wins!'
        else:
            text = 'Tie!'
        self.render_text(text, (self.w/2, self.h*0.1), BLACK_RED)


    def notify_passed_player(self, game):
        text = 'The ' + game.current_player.name + ' passes the turn.'
        self.render_text(text, (self.w/2, self.h*0.9))


    def redraw(self, game):
        if self.game.current_player.name == 'Player1':
            player1 = self.game.current_player
            player2 = self.game.another_player
        else:
            player1 = self.game.another_player
            player2 = self.game.current_player

        self.render_field(game)

        self.render_text('Player1: ' + str(player1.get_point()), (0.1*self.w, self.h*0.5))
        self.render_text('Player2: ' + str(player2.get_point()), (0.9*self.w, self.h*0.5))

        self.button('Restart', 25, 525, 100, 50, BUTTON, BUTTON_HOVER)
        self.button('Exit', 475, 525, 100, 50, BUTTON, BUTTON_HOVER)
        self.button('Player vs Player', 25, 20, 100, 25, BUTTON, BUTTON_HOVER)
        self.button('Player vs Bot', 25, 55, 100, 25, BUTTON, BUTTON_HOVER)
        # self.button('Bot vs Bot', 25, 90, 100, 25, (255,241,241), BUTTON_HOVER)


    def render_field(self, game):
        self.screen.fill((0, 160, 0))
        self.draw_field()
        self.draw_chips(game)


    def notify_incorrect_move(self, game):
        self.render_text('Incorrect move, try again!', (self.w/2, self.h*0.1))


    def notify_moving_player(self, game):
        self.render_text(game.current_player.name + ' your turn.', (self.w/2, self.h*0.9))        


    def draw_field(self):
        # define postion of the field on screen
        left, top = self.get_field_pos()
        _, height = self.get_field_size()
        cell_diff = self.get_cell_size() 

        # drawing cells
        for i in range(8):
            rleft = left + i*cell_diff
            for j in range(8):
                rtop = top + j*cell_diff
                # to make chess-like field, change colors
                color = BLACK_GREEN if (i + j) % 2 else WHITE_GREEN
                # draw cell
                pygame.draw.rect(self.screen, color, (rleft, rtop, cell_diff, cell_diff))


    def draw_chips(self, game):
        left, top = self.get_field_pos()
        cell_diff = self.get_cell_size() 

        available_moves = game.get_available_moves()

        for i in range(game.DIMENSION):
            rleft = left + i*cell_diff
            for j in range(game.DIMENSION):
                rtop = top + j*cell_diff
                # define center of a cell
                center = (rleft + cell_diff/2, rtop + cell_diff/2)
                
                # select color depends on cell type
                if (i, j) in available_moves:
                    color = BLACK_GREEN1
                elif game.board[i][j] == Cell.EMPTY:
                    continue
                elif game.board[i][j] == Cell.BLACK:
                    color = BLACK
                elif game.board[i][j] == Cell.WHITE:
                    color = WHITE        

                # draw chip
                pygame.draw.circle(self.screen,
                    color, center, cell_diff/2*0.8)


    def button(self, msg, x, y, w, h, ic, ac):
        # get mouse position and mouse pressed information
        mouse = pygame.mouse.get_pos()
        # check is mouse inside button box
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            # if mouse hover in button paint in "ac" color
            pygame.draw.rect(self.screen, ac,(x,y,w,h))
        else:
            # else paint in "ic" color
            pygame.draw.rect(self.screen, ic,(x,y,w,h))
        # render text inside button
        self.render_text(msg, (x + (w/2), y + (h/2)), font_size=12)


    def get_field_pos(self):
        return 0.2*self.w, 0.2*self.h


    def get_field_size(self):
        return 0.6*self.w, 0.6*self.h


    def get_cell_size(self):
        return self.get_field_size()[0] // 8