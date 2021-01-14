import sys
from time import sleep
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

def check_events(ai_settings, screen, stats, 
                 play_button, ship, aliens, bullets):
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
        # mouse down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, 
                              play_button, ship, aliens, 
                              bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, 
                      ship, aliens, bullets, mouse_x, mouse_y):
    '''Start new game when player clicks Play'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset game settings
        ai_settings.initialize_dynamic_settings()
        # Hide cursor
        pygame.mouse.set_visible(False)
        # Reset game stats
        stats.reset_stats()
        stats.game_active = True
        # Empty aliens, bullets
        aliens.empty()
        bullets.empty()
        # Create new fleet, center ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, 
                  aliens, bullets, play_button):
    '''Update images on screen, flip to new screen.'''
    # Redraw screen
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets (order of draw displays back--> front)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    # Draw ship, aliens, scoreboard 
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    
    # Draw play button if game inactive
    if not stats.game_active:
        play_button.draw_button()
        
    # Make most recent screen visible.
    pygame.display.flip()
    
def update_bullets(ai_settings, screen, stats, sb, 
                   ship, aliens, bullets):
    '''Update bullet positions, check collisions, 
    get rid of old bullets'''
    # Update positions
    bullets.update()   
        
    # Get rid of bullets once offscreen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(ai_settings, screen, stats, 
                                  sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, 
                                  sb, ship, aliens, bullets):
    '''Respond to bullet-alien collisions.'''
    # Remove any bullet-alien pairs that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, 
                                            True, True)
    # Increase score
    if collisions:
        stats.score += ai_settings.alien_points
        sb.prep_score()
    
    # If last alien is destroyed, create new fleet     
    if len(aliens) == 0:
        # Destroy existing bullets, speed up game, create new fleet
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
    
    
def check_fleet_edges(ai_settings, aliens):
    '''Change fleet direction if any aliens have reached an edge.'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''Drop fleet, change direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    '''Respond to ship being hit by an alien'''
    if stats.ships_left > 0:
        # Decrement ships remaining
        stats.ships_left -= 1
        # Reset game
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens) 
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    '''Check if any aliens have reached the screen bottom'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat same as ship hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''Check fleet-at-edge, update alien positions, 
    check if ship is hit.'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # Detect ship hits
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        
    # Detect aliens at bottom
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def get_number_aliens_x(ai_settings, alien_width):
    '''Find number of aliens that fit in a row'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    '''Determine number of alien rows that fit on the screen'''
    available_space_y = (ai_settings.screen_height - 
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''Create an alien, place it in row'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = (alien.rect.height + 
                    (2 * alien.rect.height * row_number))
    aliens.add(alien)          

def create_fleet(ai_settings, screen, ship, aliens):
    '''Create fleet of aliens'''
    # Create an alien
    alien = Alien(ai_settings, screen)
    
    # Find number of aliens in a row
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, 
                                  alien.rect.height)
    
    # Create fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
