"""Array utilities for efficient 2D data storage using 1D arrays.

This module provides functions to create and manipulate 2D data structures
stored as 1D arrays for improved memory efficiency. Two implementations are
provided: numpy-based (faster, single type) and list-based (slower, flexible).

Both implementations store metadata (width and height) in the first two
indices for runtime dimension information.
"""

from numpy import empty as npempty, int16, ndarray as npndarr


def create_1d_as_2d_np(width: int16, height: int16) -> npndarr:
    """Creates a 1D array that can be accessed as a 2D array for more efficient storage.

    Args:
        width (int16): The width of the 2D array.
        height (int16): The height of the 2D array.

    Returns:
        npndarr: A 1D numpy array representing a 2D array.
    """
    empty_arr = npempty(width * height + 1, dtype=int16)
    empty_arr[0] = width
    return empty_arr


def fill_np(arr: npndarr, val: int16) -> npndarr:
    """Fills the 1D-as-2D numpy array with a given value.

    Args:
        arr (npndarr): The 1D-as-2D numpy array.
        val (int16): The value to fill the array with.

    Returns:
        npndarr: The filled 1D-as-2D numpy array.
    """
    arr[1:] = val
    return arr


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
    arr[arr[0] * row + col + 1] = val
    return arr



def get_1d_as_2d_np(arr: npndarr, row: int16, col: int16) -> int16:
    """Gets the value at a given (row, col) in a 1D-as-2D numpy array.

    Args:
        arr (npndarr): The 1D-as-2D numpy array.
        row (int16): The row index.
        col (int16): The column index.

    Returns:
        int16: The value at the specified location.
    """
    return arr[arr[0] * row + col + 1]


def create_1d_as_2d_ls(width: int, height: int) -> list:
    """Creates a 1D list that can be accessed as a 2D array for flexible storage.

    Args:
        width (int): The width of the 2D array.
        height (int): The height of the 2D array.

    Returns:
        list: A 1D list representing a 2D array with None values.
    """   
    ls = []
    ls.append(width)
    for i in range(width * height):
        ls.append(None)
    return ls


def set_1d_as_2d_ls(ls: list, val, row: int, col: int) -> list:
    """Sets the value at a given (row, col) in a 1D-as-2D list.

    Args:
        ls (list): The 1D-as-2D list.
        val: The value to set (can be any type).
        row (int): The row index.
        col (int): The column index.

    Returns:
        list: The modified 1D-as-2D list.
    """
    ls[ls[0] * row + col + 1] = val
    return ls


def get_1d_as_2d_ls(ls: list, row: int, col: int):
    """Gets the value at a given (row, col) in a 1D-as-2D list.

    Args:
        ls (list): The 1D-as-2D list.
        row (int): The row index.
        col (int): The column index.

    Returns:
        Any: The value at the specified location.
    """ 
    return ls[ls[0] * row + col + 1]
