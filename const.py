import pygame

class Constants:
    def __init__(self):
        SCREEN_DIMENSIONS = (1280, 720)
        ASSETS_DIR = "assets"
        
        TILESET_FILE_NAME: str
        TILESET_FILE_EXT = ".png"
        TILESET = pygame.image.load("" + ASSETS_DIR + "/" + TILESET_FILE_NAME + TILESET_FILE_EXT).convert_alpha()
        TILE_PXL_SIZE = 4
    