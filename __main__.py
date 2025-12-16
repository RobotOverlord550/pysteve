import pygame, arr1d_as_2d, const
from numpy import array as nparray


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