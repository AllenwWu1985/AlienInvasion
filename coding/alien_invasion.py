import sys
import pygame

class AlienInvasion:
    """This is the overall class to manage game assets and behavior"""

    def __init__(self):
        """Initalize the game and creat game resource."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color
        self.bg_color=(230,230,230)

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            # Watch for mouse and key board event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__=='__main__':
    #Make game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()

