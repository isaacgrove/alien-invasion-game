import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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
    
    # Make Play button
    play_button = Button(ai_settings, screen, "Play")
    
    # Store game stats, create scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make a ship
    ship = Ship(ai_settings, screen)
    
    # Make a group to store bullets
    bullets = Group()
    
    # Make a group to store aliens
    aliens = Group()
    
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Main game loop
    while True:
        # Check for player input
        gf.check_events(ai_settings, screen, stats, 
                        play_button, ship, aliens, bullets)
        
        if stats.game_active:
            # Update element positions
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        # Draw screen
        gf.update_screen(ai_settings, screen, stats, sb, ship, 
                         aliens, bullets, play_button)

            

run_game()