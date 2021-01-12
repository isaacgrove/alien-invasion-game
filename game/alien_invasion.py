import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game
    pygame.init()
    
    # Initialize settings
    ai_settings = Settings()
    
    # Build the screen
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship
    ship = Ship(ai_settings, screen)
    
    # Make a group to store bullets
    bullets = Group()
    
    # Main game loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        
        # Get rid of bullets once offscreen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            

run_game()