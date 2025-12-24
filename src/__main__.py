import tileset
import pygame
import directory
from enum import Enum


WINDOW_DIMENSIONS = (1280, 720)
ASSETS_FOLDER_NAME = "assets"
TILESET_FILE_NAME = "tileset"
TILESET_FILE_EXT = ".png"


class TileIndex(Enum):
    AIR = 0
    GRASS = 1


assets_folder = directory.get_global_path(ASSETS_FOLDER_NAME)
tileset = tileset.Tileset(TILESET_FILE_NAME, TILESET_FILE_EXT, assets_folder, 4)

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_DIMENSIONS)
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
