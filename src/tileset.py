import pygame
import data_structures

class Tileset():
    def __init__(self, file_name: str, file_ext: str, assets_dir_global: str, tile_size_p: int):
        self.file_name = file_name
        self.file_ext = file_ext
        self.assets_dir_global = assets_dir_global
        self.tile_size_p = tile_size_p
        
        self.tileset: pygame.Surface = pygame.image.load(
            "" + self.assets_dir_global + "/" + self.file_name + self.file_ext
        )

        tileset_width_pxl = self.tileset.get_size()[0]
        tileset_height_pxl = self.tileset.get_size()[1]

        self.tiles = data_structures.ls_1d_as_2d.create(tileset_width_pxl,
                                                    tileset_height_pxl)

        for y in range(0, tileset_height_pxl, self.tile_size_p):
            for x in range(0, tileset_width_pxl, self.tile_size_p):
                self.tiles = data_structures.ls_1d_as_2d.set(
                    self.tiles,
                    self.tileset.subsurface((x, y), (self.tile_size_p,
                                                     self.tile_size_p)), y, x)
    

    def get(self, index: int):
        return data_structures.ls_1d_as_2d.get(self.tiles, index)