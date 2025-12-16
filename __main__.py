import pygame, oned_as_twod
from numpy import array as nparray

SCREEN_DIMENSIONS = (1280, 720)
ASSETS_DIR = "assets"



if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
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