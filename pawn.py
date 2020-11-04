from piece import Piece
import pygame

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, type)
        self.is_first_move = True
        self.color = color
    
    def draw_pawn(self, screen):
        if self.color == 'white':
            self.image = pygame.image.load('images/white_pawn.png')
        else:
            self.image = pygame.image.load('images/black_pawn.png')
        self.rect = self.image.get_rect()


pawn = Pawn('white')