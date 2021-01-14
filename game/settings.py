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
        self.ship_limit = 3
        
        # Bullet
        self.bullet_speed_factor = 10
        self.bullet_width = 100
        self.bullet_height = 8
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 150
        self.fleet_direction = 1    # -1 left, 1 right