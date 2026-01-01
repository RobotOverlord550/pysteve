import numpy as np
from opensimplex import OpenSimplex


def new_simplex(seed: int) -> OpenSimplex:
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
    f = frequency
    a = amplitude
    max_value = 0.0
    height, width = grid.shape
    noise_arr = np.zeros((height, width))
    for _ in range(octaves):
        max_value += a
        noise2_add_octave(
            height=height,
            width=width,
            frequency=f,
            amplitude=a,
            start_arr=noise_arr,
            simplex=simplex,
        )
        f *= lacunarity
        a *= persistance
        
        print(f"Octave complete | Frequency: {f} | Amplitude: {a} | Max Value: {max_value}")
        
    for row in range(height):
        for col in range(width):
            norm_value = (noise_arr[row, col] + max_value) / (2 * max_value)
            if norm_value > threshold:
                grid[row, col] = new_val
            print(f"Set tilemap[{row}, {col}] to {grid[row, col]} based on normalized value {norm_value}")
    
    print("Cave generation complete")
            
            
def noise2_add_octave(
    height,
    width,
    frequency: float,
    amplitude: float,
    start_arr: np.ndarray,
    simplex: OpenSimplex,
):
    noise_arr = start_arr
    f = frequency
    a = amplitude
    
    for y in range(height):
        for x in range(width):
            noise_value = simplex.noise2(x=x * f, y=y * f)
            noise_arr[y, x] += noise_value * a
            print(f"Overlaying noise at ({y}, {x}): noise_value={noise_value}, updated_noise_arr={noise_arr[y, x]}")
    print("Noise overlay complete")