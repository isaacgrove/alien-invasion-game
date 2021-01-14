# Settings

class Settings():
    '''Stores all settings for Alien Invasion'''
    
    def __init__(self):
        '''Initialize the game's static settings.'''
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (245, 245, 245)
        
        # Ship
        self.ship_limit = 3
        
        # Bullets
        self.bullet_width = 100
        self.bullet_height = 8
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # Aliens
        self.fleet_drop_speed = 30
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        '''Initialize settings that change midgame'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 0.5
        self.fleet_direction = 1    # -1 left, 1 right
        #Scoring
        self.alien_points = 10
    
    def increase_speed(self):
        '''Increase speed settings and point values'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self. alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * 
                                self.score_scale)