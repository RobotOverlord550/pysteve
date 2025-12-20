"""Game constants and tileset management.

This module defines the Constants class which handles game configuration,
including screen dimensions, tileset loading, and tile management. The tileset
is loaded from assets and parsed into individual tile data structures for
efficient game rendering.
"""

import arr1d_as_2d
import pygame
import os


class Constants:
    """Manages game configuration and tileset data.

    Attributes:
        SCREEN_DIMENSIONS (tuple): Width and height of the game window.
        TILESET (pygame.Surface): The loaded tileset image.
        TILES (list): 1D-as-2D array storing individual tile surfaces.
        TILE_PXL_SIZE (int): Size of each tile in pixels.
        WORLD_DIM (tuple): Width and height of the game world in tiles.
    """   
    def load_tiles(self):
        """Loads and parses tileset into individual tile surfaces.

        This method iterates through the tileset image and extracts individual
        tile subsurfaces based on TILE_PXL_SIZE. Each tile is stored in the
        TILES 1D-as-2D array.
        """     
        tiles = arr1d_as_2d.create_1d_as_2d_np(self.TILESET.get_width(),
                                               self.TILESET.get_height())

        for y in range(0, self.TILESET.get_height(), self.TILE__PXL_SIZE):
            for x in range(0, self.TILESET.get_width(), self.TILE__PXL_SIZE):
                arr1d_as_2d.set_1d_as_2d_np(
                    tiles, self.TILESET.subsurface(
                        (x, y, self.TILE__PXL_SIZE, self.TILE_PXL_SIZE)))

    def __init__(self):
        """Initializes game constants and loads tileset data.

        Sets up screen dimensions, loads the tileset image from assets,
        parses tiles into the TILES array, and initializes world dimensions.
        """
        self.SCREEN_DIMENSIONS = (1280, 720)
        self.ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

        self.TILESET_FILE_NAME = "tileset"
        self.TILESET_FILE_EXT = ".png"
        self.TILESET: pygame.Surface = pygame.image.load(
            "" + self.ASSETS_DIR + "/" + self.TILESET_FILE_NAME + self.TILESET_FILE_EXT
        )
        self.TILE_PXL_SIZE = 4

        tileset_width_pxl = self.TILESET.get_size()[0]
        tileset_height_pxl = self.TILESET.get_size()[1]

        self.TILES = arr1d_as_2d.create_1d_as_2d_ls(tileset_width_pxl,
                                                    tileset_height_pxl)

        for y in range(0, tileset_height_pxl, self.TILE_PXL_SIZE):
            for x in range(0, tileset_width_pxl, self.TILE_PXL_SIZE):
                self.TILES = arr1d_as_2d.set_1d_as_2d_ls(
                    self.TILES,
                    self.TILESET.subsurface((x, y), (self.TILE_PXL_SIZE,
                                                     self.TILE_PXL_SIZE)), y, x)

        self.WORLD_DIM = (512, 256)
