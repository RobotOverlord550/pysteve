from numpy import array as nparray, int16

class TileMap:
    def __init__(self, x_dimension: int, y_dimension: int):
        self.map = nparray(dtype=int16, [])