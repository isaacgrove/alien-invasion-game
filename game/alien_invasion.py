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
        # Check for player input
        gf.check_events(ai_settings, screen, ship, bullets)
        
        # Update ship, bullet positions
        ship.update()
        gf.update_bullets(bullets)
        
        # Draw screen
        gf.update_screen(ai_settings, screen, ship, bullets)

            

run_game()