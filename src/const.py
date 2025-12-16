# TODO document

# imports
import arr1d_as_2d
import logging
import pygame
import os


class Constants:
    # Load tiles from tileset image
    def load_tiles(self):
        """_summary_
        """        
        # Create 1D-as-2D numpy array for tiles
        tiles = arr1d_as_2d.create_1d_as_2d_np(self.TILESET.get_width(),
                                               self.TILESET.get_height())

        # Populate tiles array
        for y in range(0, self.TILESET.get_height(), self.TILE__PXL_SIZE):
            for x in range(0, self.TILESET.get_width(), self.TILE__PXL_SIZE):
                arr1d_as_2d.set_1d_as_2d_np(
                    tiles, self.TILESET.subsurface(
                        (x, y, self.TILE__PXL_SIZE, self.TILE_PXL_SIZE)))

    # Initialize constants

    def __init__(self):
        """_summary_
        """        
        self.SCREEN_DIMENSIONS = (1280, 720)
        self.ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

        self.TILESET_FILE_NAME = "tileset"
        self.TILESET_FILE_EXT = ".png"
        # Load tileset image as pygame surface
        self.TILESET: pygame.Surface = pygame.image.load(
            "" + self.ASSETS_DIR + "/" + self.TILESET_FILE_NAME + self.TILESET_FILE_EXT
        )
        # Tile pixel size (height and width)
        self.TILE_PXL_SIZE = 4

        # reference variables for the rest of the function
        tileset_width_pxl = self.TILESET.get_size()[0]
        tileset_height_pxl = self.TILESET.get_size()[1]

        # Create a 1D list which acts like a 2D list for tiles
        self.TILES = arr1d_as_2d.create_1d_as_2d_ls(tileset_width_pxl,
                                                    tileset_height_pxl)

        # Populate tiles list
        for y in range(0, tileset_height_pxl, self.TILE_PXL_SIZE):
            for x in range(0, tileset_width_pxl, self.TILE_PXL_SIZE):
                self.TILES = arr1d_as_2d.set_1d_as_2d_ls(
                    self.TILES,
                    self.TILESET.subsurface((x, y), (self.TILE_PXL_SIZE,
                                                     self.TILE_PXL_SIZE)), y, x)

        # World dimensions in tiles
        self.WORLD_DIM = (512, 256)
