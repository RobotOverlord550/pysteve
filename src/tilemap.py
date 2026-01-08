import numpy as np


def create(
        height: int,
        width: int
        ) -> np.ndarray:
    """create new tilemap

    Args:
        height (int): tilemap height
        width (int): tilemap width

    Returns:
        np.ndarray: tilemap represented as a numpy ndarray"""
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
        tile_index (int): _description_"""
    tilemap[:, :] = tile_index


def fill_subsection(
    tilemap: int,
    tile_index: int,
    subsection_tl_row: int,
    subsection_tl_col: int,
    subsection_br_row: int,
    subsection_br_col: int
):
    """fills a subsection of the tilemap using position parameters

    Args:
        tilemap (int): tilemap to change
        tile_index (int): tile index to set subsection to
        subsection_tl_row (int): top left row of subsection
        subsection_tl_col (int): top left collumn of subsection
        subsection_br_row (int): bottom right row of subsection
        subsection_br_col (int): bottom right collumn of subsection"""
    for row in range(subsection_tl_row, subsection_br_row):
        for col in range(subsection_tl_col, subsection_br_col):
            tilemap[row, col] = tile_index
