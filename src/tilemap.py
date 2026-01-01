import numpy as np
from opensimplex import OpenSimplex


def create(
        height: int,
        width: int
    ) -> np.ndarray:
    arr = np.array([[0 for _ in range(height)] for _ in range(width)])

    print("Created tilemap of size:", arr.shape)
    return arr


def set_tile(
        tilemap,
        row: int,
        col: int,
        tile_index: int,
        verbose: bool = False
    ):
    tilemap[row, col] = tile_index
    if verbose:
        print(f"Set tile at ({row}, {col}) to index {tile_index}")


def fill(
        tilemap,
        tile_index: int
    ):
    # Vectorized fill: assign the tile_index to the entire array at once.
    tilemap[:, :] = tile_index
    print(f"Filled tilemap with tile index {tile_index}")
    
    