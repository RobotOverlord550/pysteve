import pygame
import arr1d_as_2d

class Constants:
    def load_tiles(self):
        tiles = arr1d_as_2d.create_1d_as_2d_np(self.TILESET.get_width(), 
                                               self.TILESET.get_heightw)

        for y in range(0, self.TILESET.get_height(), self.TILE__PXL_SIZE):
            for x in range(0, self.TILESET.get_width(), self.TILE__PXL_SIZE):
                arr1d_as_2d.set_1d_as_2d_np(
                    tiles, self.TILESET.subsurface(
                        (x, y, self.TILE__PXL_SIZE, self.TILE_PXL_SIZE)))
        
    
    def __init__(self):
        self.SCREEN_DIMENSIONS = (1280, 720)
        self.ASSETS_DIR = "assets"
        
        self.TILESET_FILE_NAME: str
        self.TILESET_FILE_EXT = ".png"
        self.TILESET: pygame.Surface = pygame.image.load(
            "" + self.ASSETS_DIR + "/" + self.TILESET_FILE_NAME + self.TILESET_FILE_EXT
            ).convert_alpha()
        self.TILE_PXL_SIZE = 4
        tileset_width_pxl = self.TILESET.get_size().x
        tileset_height_pxl = self.TILESET.get_size().y
        self.TILES = arr1d_as_2d.create_1d_as_2d_ls(tileset_width_pxl, 
                                                    tileset_height_pxl)
         
        for y in range(0, tileset_height_pxl, self.TILE_PXL_SIZE):
            for x in range(0, tileset_width_pxl, self.TILE_PXL_SIZE):
                self.TILES = arr1d_as_2d.set_1d_as_2d_ls(
                    self.TILES, 
                    self.TILESET.subsurface(
                        (x, y), 
                        self.TILE_PXL_SIZE, 
                        self.TILE_PXL_SIZE))
                
        self.WORLD_DIM = (512, 256)