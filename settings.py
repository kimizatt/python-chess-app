class Settings: 
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1600
        self.screen_height = 1000
        self.bg_color = (110, 90, 130)
        
        # Square settings
        self.light_square = (200, 196, 204 )
        self.dark_square = (83, 83, 83)
        self.square_width = 100