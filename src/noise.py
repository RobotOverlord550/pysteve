import numpy as np
from opensimplex import OpenSimplex


def new_simplex(seed: int) -> OpenSimplex:
    """create noise function with game seed

    Args:
        seed (int): Game Seed
    Returns:
        OpenSimplex: Initialized noise function
    """    
    opensimplex = OpenSimplex(seed=seed)
    return opensimplex


def generate_noise2(
    grid: np.ndarray,
    frequency: float,
    amplitude: float,
    lacunarity: float,
    persistance: float,
    octaves: int,
    simplex: OpenSimplex,
    new_val: int, 
    threshold: float
):
    """applies noise algorithm to 2d integer array

    Args:
        grid (np.ndarray): starting 2d array
        frequency (float): frequency of noise algorithm (0-1)
        amplitude (float): amplitude of noise algorithm (0-1)
        lacunarity (float): lacunarity of noise algorithm (0-1)
        persistance (float): persistence of noise algorithm (0-1)
        octaves (int): octaves of noise algorithm (>0)
        simplex (OpenSimplex): initialized simplex object (use new_simplex())
        new_val (int): value to change grid cells to when the cells are greater than the threshold
        threshold (float): threshold for determining what cells are changed
    """
    # set initial variables   
    f = frequency
    a = amplitude
    max_value = 0.0
    height, width = grid.shape
    noise_arr = np.zeros((height, width))
    
    # runs noise algorithm for set number of Octaves
    for _ in range(octaves):
        max_value += a
        _noise2_add_octave(
            frequency=f,
            amplitude=a,
            start_arr=noise_arr,
            simplex=simplex,
        )
        f *= lacunarity
        a *= persistance
        print(f"octave {_ + 1} complete")
    
    # normalize calculated values and set values in grid that are above the threshold to the new value
    for row in range(height):
        for col in range(width):
            norm_value = (noise_arr[row, col] + max_value) / (2 * max_value)
            if norm_value > threshold:
                grid[row, col] = new_val
            
            
def _noise2_add_octave(
    frequency: float,
    amplitude: float,
    start_arr: np.ndarray,
    simplex: OpenSimplex,
):
    """helper function for generate_noise_2() to apply octaves

    Args:
        frequency (float): frequency of octave
        amplitude (float): amplitude of octave
        start_arr (np.ndarray): array to apply octave too
        simplex (OpenSimplex): initialized simplex object to use
    """
    # initial variables
    noise_arr = start_arr
    f = frequency
    a = amplitude
    
    # apply noise to all grid cells
    for y in range(noise_arr.shape[0]):
        for x in range(noise_arr.shape[1]):
            noise_value = simplex.noise2(x=x * f, y=y * f)
            noise_arr[y, x] += noise_value * a