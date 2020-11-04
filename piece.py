from pawn import Pawn
from pygame.sprite import Sprite

class Piece(Sprite):
    def __init__(self, color, type):
        self.color = color
        self.type = type
        self.start_x = 0
        self.start_y = 0
        self.is_alive = True
        self.end_x = ''
        self.end_y = ''
        self.image = ''
        self.current_x = 0
        self.current_y = 0

    def __repr__(self):
        print(f"{self.color} {self.start_x}{self.start_y}")

    def create_piece(self):
        if type == 'pawn':
            pawn = Pawn(self.color)

    def load_pieces(self, screen):
        pass
        


