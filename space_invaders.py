import sys

import pygame


class SpaceInvaders:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Space Invaders!")
        self.clock = pygame.time.Clock() # creating a clock to manage the correct frame rate

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60) # Stablish the clock to maintain 60 times per second

if __name__ == '__main__':
    # Make a game instance, and run the game.
    si = SpaceInvaders()
    si.run_game()