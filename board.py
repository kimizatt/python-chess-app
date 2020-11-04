from square import Square
import pygame
from settings import Settings


class Board:
    def __init__(self):
        horizontal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        vertical = range(1, 9)
        colors = ['dark', 'light']
        all_squares = [Square(x, y, color)
                       for x in horizontal for y in vertical for color in colors]
        self.squares = [square for square in all_squares if (
            square.horizontal in 'ACEG' and square.vertical % 2 == 1 and square.color == 'light'
            or square.horizontal in 'ACEG' and square.vertical % 2 == 0 and square.color == 'dark'
            or square.horizontal in 'BDFH' and square.vertical % 2 == 1 and square.color == 'dark'
            or square.horizontal in 'BDFH' and square.vertical % 2 == 0 and square.color == 'light')]

        self.settings = Settings()
        # print(self.squares)
        # print(len(self.squares))

    def display_board(self, screen):
        for square in self.squares:
            if square.horizontal == "A":
                x = 400
            elif square.horizontal == "B":
                x = 500
            elif square.horizontal == "C":
                x = 600
            elif square.horizontal == "D":
                x = 700
            elif square.horizontal == "E":
                x = 800
            elif square.horizontal == "F":
                x = 900
            elif square.horizontal == "G":
                x = 1000
            elif square.horizontal == "H": 
                x = 1100

            y = 100 * square.vertical
            if square.color == "light":
                pygame.draw.rect(screen, self.settings.light_square, [x, y, self.settings.square_width, self.settings.square_width] )
            elif square.color == "dark":
                pygame.draw.rect(screen, self.settings.dark_square, [x, y, self.settings.square_width, self.settings.square_width])

board = Board()
