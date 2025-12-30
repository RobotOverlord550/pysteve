import numpy as np
from opensimplex import OpenSimplex


def init_perlin(seed=0) -> OpenSimplex:
    print("Initialized Perlin noise generator")
    return OpenSimplex(seed=seed)


def create(
        height: int,
        width: int
    ) -> np.ndarray:
    arr = np.array([[0 for _ in range(width)] for _ in range(height)])

    print("Created tilemap of size:", arr.shape)
    return arr


def surface_from_value(value: int | float | None, height: int) -> int:
    if value is None:
        return 0
    if isinstance(value, float):
        row = int(value * (height - 1))
    else:
        row = int(value)
    return max(0, min(row, height - 1))


def set_tile(
        tilemap,
        x: int,
        y: int,
        tile_index: int,
        verbose: bool = False
    ):
    tilemap[y, x] = tile_index
    if verbose:
        print(f"Set tile at ({x}, {y}) to index {tile_index}")


def fill(
        tilemap,
        tile_index: int
    ):
    # Vectorized fill: assign the tile_index to the entire array at once.
    tilemap[:, :] = tile_index
    print(f"Filled tilemap with tile index {tile_index}")


def apply_noise(
    tilemap: np.ndarray,
    scale: float,
    octaves: int,
    opensimplex: OpenSimplex,
    min_row: int,
    max_row: int,
    below_index: int, 
):
    for col in range(tilemap.shape[1]):
        noise_values = np.array([
            opensimplex.noise2(x=col / scale, y=row / scale)
            for row in range(tilemap.shape[0])
        ])
        normalized = (noise_values + 1) / 2
        surface_rows = (normalized * (max_row - min_row) + min_row).astype(int)

        for row in range(tilemap.shape[0]):
            if row >= surface_rows[row]:
                tilemap[row, col] = below_index