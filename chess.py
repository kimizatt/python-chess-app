import sys
import pygame
from settings import Settings
from board import Board
# from piece import Piece

class Chess:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Chess")

        # self.pieces = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            board = Board()
            # white_piece = Piece('white', 'pawn')
            # black_piece = Piece('black', 'pawn')
            # board.display_board(self.screen)
            # white_piece.load_pieces(self.screen)
            # black_piece.load_pieces(self.screen)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def set_board(self):
        pass



if __name__ == '__main__':
    #Make a game instance, and run the game.
    chess = Chess()
    chess.run_game()


