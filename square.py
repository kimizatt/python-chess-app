class Square:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.isOccupied = False
        self.color = color

    def __repr__(self):
        return f"{self.horizontal}{self.vertical} {self.color}"
