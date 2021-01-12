import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''Respond to keypresses'''
    if event.key == pygame.K_RIGHT:
        # Move right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move left.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def fire_bullet(ai_settings, screen, ship, bullets):
    '''Fire a bullet if limit not reached'''
    # Create new bullet, add to bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)    
    
def check_keyup_events(event, ship):
    '''Respond to key releases'''
    if event.key == pygame.K_RIGHT:
        # Move right.
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Move left.
        ship.moving_left = False   

def check_events(ai_settings, screen, ship, bullets):
    '''Respond to keypresses and mouse events.'''
    for event in pygame.event.get(): # dumps event queue
        # quit game
        if event.type == pygame.QUIT:
            sys.exit()
        # key down (R/L)  
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, 
                                 bullets)

        # key up (R/L)    
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    '''Update images on screen, flip to new screen.'''
    # Redraw screen
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets (behind ship and aliens)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    aliens.draw(screen)
    
    # Make most recent screen visible.
    pygame.display.flip()
    
def update_bullets(bullets):
    '''Update bullet positions, get rid of old bullets'''
    # Update positions
    bullets.update()   
         
    # Get rid of bullets once offscreen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_fleet(ai_settings, screen, aliens):
    '''Create a full fleet of aliens'''
    # create an alien and find the number of aliens in a row
    # Spacing between aliens = 1 alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width
    number_aliens_x = int(available_space_x / (alien_width))
    
    # create first row of aliens
    for alien_number in range(number_aliens_x):
        # Create an alien, place it in row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width * alien_number + 50
        alien.rect.x = alien.x
        aliens.add(alien)