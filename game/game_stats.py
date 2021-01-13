class GameStats():
    '''Track statistics for Alien Invasion'''
    
    def __init__(self, ai_settings):
        '''Initialize statistics.'''
        self.ai_settings = ai_settings
        self.reset_stats()
        
    def reset_stats(self):
        '''Initialize stats that can change mid-game'''
        self.ships_left = self.ai_settings.ship_limit