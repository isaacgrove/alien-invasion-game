# Settings

class Settings():
    '''Stores all settings for Alien Invasion'''
    
    def __init__(self):
        '''Initialize the game's settings.'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (245, 245, 245)
        
        # Ship
        self.ship_speed_factor = 1.5
        
        # Bullet
        self.bullet_speed_factor = 2.5
        self.bullet_width = 6
        self.bullet_height = 8
        self.bullet_color = 60, 60, 60