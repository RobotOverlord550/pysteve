import numpy as np
from opensimplex import OpenSimplex


def new_simplex(seed: int) -> OpenSimplex:
    opensimplex = OpenSimplex(seed=seed)
    return opensimplex


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


def generate_caves(
    tilemap: np.ndarray,
    frequency: float,
    amplitude: int,
    lacunarity: float,
    persistance: float,
    octaves: int,
    simplex: OpenSimplex,
    below_index: int, 
    below_value: float
):
    f = frequency
    a = amplitude
    max_value = 0
    height, width = tilemap.shape
    noise_arr = np.zeros((height, width))
    for _ in range(octaves):
        max_value += noise2_arr_overlay(
            height=height,
            width=width,
            frequency=f,
            amplitude=a,
            max_value=max_value,
            start_arr=noise_arr,
            simplex=simplex,
        )
        f *= lacunarity
        a *= persistance
        
    for row in range(height):
        for col in range(width):
            norm_value = (noise_arr[row, col] + max_value) / (2 * max_value)
            if norm_value < below_value:
                tilemap[row, col] = below_index
            
            
def noise2_arr_overlay(
    height,
    width,
    frequency: float,
    amplitude: int,
    max_value: float,
    start_arr: np.ndarray,
    simplex: OpenSimplex,
) -> float:
    noise_arr = start_arr
    f = frequency
    a = amplitude
    
    for y in range(height):
        for x in range(width):
            noise_value = simplex.noise2(x=x * f, y=y * f)
            noise_arr[y, x] += noise_value * a
            max_value += a
    
    return max_value
    
    