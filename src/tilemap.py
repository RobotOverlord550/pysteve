import numpy as np
from opensimplex import OpenSimplex


def create(
        height: int,
        width: int
    ) -> np.ndarray:
    """create new tilemap

    Args:
        height (int): tilemap height
        width (int): tilemap width

    Returns:
        np.ndarray: tilemap represented as a numpy ndarray
    """
    # set 2d array to hold tilemap
    arr = np.array([[0 for _ in range(height)] for _ in range(width)])
    
    return arr


def set_tile(
        tilemap,
        row: int,
        col: int,
        tile_index: int,
    ):
    """change the tile at the specified row and collumn

    Args:
        tilemap (_type_): tilemap to edit
        row (int): row to use
        col (int): collumn to use
        tile_index (int): new tile
    """
    tilemap[row, col] = tile_index


def fill(
        tilemap,
        tile_index: int
    ):
    """fills tilemap with same tile.  usefull for initialization 

    Args:
        tilemap (_type_): _description_
        tile_index (int): _description_
    """    
    tilemap[:, :] = tile_index
    
    