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
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color) 
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

            # Stablish the clock to maintain 60 times per second
            self.clock.tick(60) 
            

if __name__ == '__main__':
    # Make a game instance, and run the game.
    si = SpaceInvaders()
    si.run_game()