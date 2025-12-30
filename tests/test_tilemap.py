import unittest
import sys
import os
import numpy as np

# Ensure `src` directory is on sys.path so tests can import project modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import tilemap


class TestApplyNoise(unittest.TestCase):
    def test_min_max_surface_clamping(self):
        height = 40
        width = 10
        tm = tilemap.create(height, width)
        # Use narrow min/max fractions to force clamping
        min_frac = 0.3
        max_frac = 0.6
        below = 2
        above = 1

        tm = tilemap.apply_noise(
            tilemap=tm,
            scale=20.0,
            octaves=3,
            above_index=above,
            below_index=below,
            min_surface=min_frac,
            max_surface=max_frac,
        )

        min_row = int(min_frac * (height - 1))
        max_row = int(max_frac * (height - 1))

        # For each column, find the first row that equals `below` and
        # assert it lies within [min_row, max_row]
        for x in range(width):
            col = tm[:, x]
            # convert to plain ndarray if it's a matrix-like
            col_arr = np.array(col).flatten()
            below_indices = np.where(col_arr == below)[0]
            self.assertTrue(below_indices.size > 0, f"No below tile in column {x}")
            first_below = int(below_indices[0])
            self.assertGreaterEqual(first_below, min_row)
            self.assertLessEqual(first_below, max_row)


if __name__ == '__main__':
    unittest.main()
