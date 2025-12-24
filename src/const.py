from data_structures import ls_1d_as_2d, nparr_1d_as_2d
import pygame
import os


class Constants:
    def load_tiles(self):   
        tiles = nparr_1d_as_2d.create_1d_as_2d_np(self.TILESET.get_width(),
                                               self.TILESET.get_height())

        for y in range(0, self.TILESET.get_height(), self.TILE__PXL_SIZE):
            for x in range(0, self.TILESET.get_width(), self.TILE__PXL_SIZE):
                nparr_1d_as_2d.set_1d_as_2d_np(
                    tiles, self.TILESET.subsurface(
                        (x, y, self.TILE__PXL_SIZE, self.TILE_PXL_SIZE)))

    def __init__(self):
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

        self.TILES = ls_1d_as_2d.create_1d_as_2d_ls(tileset_width_pxl,
                                                    tileset_height_pxl)

        for y in range(0, tileset_height_pxl, self.TILE_PXL_SIZE):
            for x in range(0, tileset_width_pxl, self.TILE_PXL_SIZE):
                self.TILES = ls_1d_as_2d.set_1d_as_2d_ls(
                    self.TILES,
                    self.TILESET.subsurface((x, y), (self.TILE_PXL_SIZE,
                                                     self.TILE_PXL_SIZE)), y, x)

        self.WORLD_DIM = (512, 256)
