from numpy import ndarray as npndarr
import arr1d_as_2d
from __main__ import CONSTANTS
from enums import TileIndex

class world:
    def __init__(self):
        self.world_tilemap: npndarr = arr1d_as_2d.create_1d_as_2d_np(
            CONSTANTS.WORLD_DIM[0], CONSTANTS.WORLD_DIM[1])
        arr1d_as_2d.fill_1d_as_2d_np(self.world_tilemap, TileIndex.GRASS)