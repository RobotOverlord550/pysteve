from numpy import array as nparray, int16
import pygame

TILESET_FILE_NAME = "tileset"
TILESET_FILE_EXT = ".png"
TILESET = pygame.image.load("" + ASSETS_DIR + "/" + TILESET_FILE_NAME + TILESET_FILE_EXT).convert_alpha()
TILE_PXL_SIZE = 4

# Init tiles
tiles = oned_as_twod.npempty(TILESET.get_height(), TILESET.get_width())

class TileMap:
    def __init__(self, x_dimension: int, y_dimension: int):
        self.map = nparray(dtype=int16, [])