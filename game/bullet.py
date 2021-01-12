import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    ''' A class to manage bullets fired from ship'''
    
    def __init__(self, ai_settings, screen, ship):
        '''Create bullet object at ship's current position.'''
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Create bullet rect at (0, 0) then set correct pos.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store bullet's position as a decimal
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        '''Move bullet up the screen'''
        # Update bullet position
        self.y -= self.speed_factor
        # Update rect position
        self.rect.y = self.y
            
        
    def draw_bullet(self):
        '''Draw bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)