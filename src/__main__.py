import pygame
import const
import cam


CONSTANTS = const.Constants()


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(CONSTANTS.SCREEN_DIMENSIONS)
    clock = pygame.time.Clock()
    main_camera = cam.Camera(CONSTANTS.SCREEN_DIMENSIONS[0], CONSTANTS.SCREEN_DIMENSIONS[1])
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
