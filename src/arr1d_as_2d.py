# imports
from numpy import empty as npempty, int16, ndarray as npndarr


# Numpy functions (more efficient but only one type)
# Create 1D-as-2D numpy array
def create_1d_as_2d_np(width: int16, height: int16) -> npndarr:
    """Creates a 1D array that can be accessed as a 2D array for more efficient storage.

    Args:
        width (int16): The width of the 2D array.
        height (int16): The height of the 2D array.

    Returns:
        npndarr: A 1D numpy array representing a 2D array.
    """
    empty_arr = npempty(width * height + 2, dtype=int16)
    empty_arr[0] = width
    empty_arr[1] = height
    return empty_arr


# Set value at (row, col) in 1D-as-2D numpy array
def set_1d_as_2d_np(arr: npndarr, val: int16, row: int16, col: int16) -> npndarr:
    """Sets the value at a given (row, col) in a 1D-as-2D numpy array.

    Args:
        arr (npndarr): The 1D-as-2D numpy array.
        val (int16): The value to set.
        row (int16): The row index.
        col (int16): The column index.

    Returns:
        npndarr: The modified 1D-as-2D numpy array.
    """
    arr[arr[0] * row + col + 2] = val
    return arr


# Get value at (row, col) in 1D-as-2D numpy array
def get_1d_as_2d_np(arr: npndarr, row: int16, col: int16) -> int16:
    return arr[arr[0] * row + col + 2]


# Built in python list functions (less efficient but more than one type)
# Create 1D-as-2D list
def create_1d_as_2d_ls(width: int, height: int) -> list:
    ls = []
    ls.append(width)
    ls.append(height)
    for i in range(width * height):
        ls.append(None)
    return ls


# Set value at (row, col) in 1D-as-2D list
def set_1d_as_2d_ls(ls: list, val, row: int, col: int) -> list:
    ls[ls[0] * row + col + 2] = val
    return ls


# Get value at (row, col) in 1D-as-2D list
def get_1d_as_2d_ls(ls: list, row: int, col: int):
    return ls[ls[0] * row + col + 2]
