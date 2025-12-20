"""Main entry point for the Terraria clone game.

This module initializes the Pygame engine, creates the game window, and runs
the main game loop. The game continues until the user closes the window.
"""

import pygame
import const


CONSTANTS = const.Constants()


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(CONSTANTS.SCREEN_DIMENSIONS)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
