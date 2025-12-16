# imports
import pygame
import const


# Global constants instance
CONSTANTS = const.Constants()


# Main game loop
if __name__ == "__main__":
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode(CONSTANTS.SCREEN_DIMENSIONS)
    clock = pygame.time.Clock()
    running = True

    # Main loop
    while running:
        # Event handling for pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen by setting it to black
        screen.fill("black")

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 FPS
        clock.tick(60)

    # Quit pygame on exit window
    pygame.quit()
