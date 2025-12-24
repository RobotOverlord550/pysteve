from numpy import empty as npempty, int16, ndarray as npndarr
from testing import AbstractTest


class nparr_1d_as_2d:
    def create(width: int16, height: int16) -> npndarr:
        empty_arr = npempty(width * height + 1, dtype=int16)
        empty_arr[0] = width
        return empty_arr


    def fill(arr: npndarr, val: int16) -> npndarr:
        arr[1:] = val
        return arr


    def set(arr: npndarr, val: int16, row: int16, col: int16) -> npndarr:
        arr[arr[0] * row + col + 1] = val
        return arr



    def get(arr: npndarr, row: int16, col: int16) -> int16:
        return arr[arr[0] * row + col + 1]




class ls_1d_as_2d:
    def create(width: int, height: int) -> list: 
        ls = []
        ls.append(width)
        for i in range(width * height):
            ls.append(None)
        return ls


    def set(ls: list, val, row: int, col: int) -> list:
        ls[ls[0] * row + col + 1] = val
        return ls


    def get(ls: list, row: int, col: int):
        return ls[ls[0] * row + col + 1]
    



class Test(AbstractTest):
    def test_1d_as_2d_np(self):
        test_np = nparr_1d_as_2d.create(1000, 1000)
        self.assertIsNotNone(test_np)
        self.assertEqual(nparr_1d_as_2d.get(test_np, 500, 500), 0)
        test_np = nparr_1d_as_2d.set(test_np, 79, 500, 500)
        self.assertEqual(nparr_1d_as_2d.get(test_np, 500, 500), 79)


    def test_1d_as_2d_ls(self):
        test_str = "Hello World!"
        test_ls = ls_1d_as_2d.create(1000, 1000)
        self.assertIsNotNone(test_ls)
        self.assertEqual(ls_1d_as_2d.get(test_ls, 500, 500), None)
        test_ls = ls_1d_as_2d.set(test_ls, test_str, 500, 500)
        self.assertEqual(ls_1d_as_2d.get(
            test_ls, 500, 500), test_str)
