# TODO Document

from numpy import empty as npempty, int16 as i16, ndarray as npndarr


# Numpy functions (more efficient but only one type)
def create_1d_as_2d_np(width: i16, height: i16) -> npndarr:
    empty_arr = npempty(width * height + 2, dtype=i16)
    empty_arr[0] = width
    empty_arr[1] = height
    return empty_arr


def set_1d_as_2d_np(arr: npndarr, val: i16, row: i16, col: i16) -> npndarr:
    arr[arr[0] * row + col + 2] = val
    return arr
    
    
def get_1d_as_2d_np(arr: npndarr, row: i16, col: i16) -> i16:
    return arr[arr[0] * row + col + 2]


# Built in python list functions (less efficient but more than one type)
def create_1d_as_2d_ls(width: int, height: int) -> list:
    ls = []
    ls.append(width)
    ls.append(height)
    for i in range(width * height):
        ls.append(None)    
    return ls


def set_1d_as_2d_ls(ls: list, val, row: int, col: int) -> list:
    ls[ls[0] * row + col + 2] = val
    return ls


def get_1d_as_2d_ls(ls: list, row: int, col: int):
    return ls[ls[0] * row + col + 2]
    