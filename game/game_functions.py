import sys
import pygame

def check_keydown_events(event, ship):
    '''Respond to keypresses'''
    if event.key == pygame.K_RIGHT:
        # Move right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move left.
        ship.moving_left = True  
        
def check_keyup_events(event, ship):
    '''Respond to key releases'''
    if event.key == pygame.K_RIGHT:
        # Move right.
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Move left.
        ship.moving_left = False   

def check_events(ship):
    '''Respond to keypresses and mouse events.'''
    for event in pygame.event.get(): # dumps event queue
        # quit game
        if event.type == pygame.QUIT:
            sys.exit()
        # key down (R/L)  
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        # key up (R/L)    
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    '''Update images on screen, flip to new screen.'''
    # Redraw screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # Make most recent screen visible.
    pygame.display.flip()