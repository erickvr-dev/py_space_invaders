import sys

import pygame

from settings import Settings

from ship import Ship

class SpaceInvaders:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()
        
        self.clock = pygame.time.Clock() # creating a clock to manage the correct frame rate
        
        self.settings = Settings() #A instance of Settings is created
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Space Invaders! by Sp0ck")

        self.ship = Ship(self) # creates a ship object giving self reference to the game.
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            self._update_screen()

            # Stablish the clock to maintain 60 times per second
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    self.ship.rect.x += 1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color) 
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
            

if __name__ == '__main__':
    # Make a game instance, and run the game.
    si = SpaceInvaders()
    si.run_game()