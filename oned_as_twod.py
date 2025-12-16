from numpy import empty as npempty, int16 as i16, ndarray as npndarr

def create_1d_as_2d(width: int, height: int):
    return npempty(width * height, dtype=i16)

def set_1d_as_2d(arr: npndarr, val, width: int, row: int, col: int):
    arr[width * row + col] = val
    
def get_1d_as_2d(arr: npndarr, width: int, row: int, col: int):
    return arr[width * row + col]