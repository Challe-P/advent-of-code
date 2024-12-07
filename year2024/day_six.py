"""Solves the puzzles for day six 2024"""

import itertools
import numpy as np
from utils import day


class DaySix(day.Day):
    """Solves the puzzles for day six 2024"""

    directions = {"up": [-1, 0], "right": [0, 1], "down": [1, 0], "left": [0, -1]}

    def __init__(self, year=2024, date=6, data=None):
        super().__init__(year, date, data)

    def solve_a(self):
        map_of_lab = np.array([list(line) for line in self.parsed_data])
        start = np.where(map_of_lab == "^")
        map_of_lab = self.fill_map_with_x(map_of_lab, start)
        res = np.count_nonzero(map_of_lab == "X")

        return res

    def fill_map_with_x(self, map_of_lab, pos, iter_dict=None):
        """Fills the map with X where the guard walks."""
        if iter_dict is None:
            iter_dict = itertools.cycle(self.directions.items())
        direction = next(iter_dict)
        while map_of_lab[pos] != "#":
            map_of_lab[pos] = "X"
            pos = pos[0] + direction[1][0], pos[1] + direction[1][1]
            if not self.in_range(pos, map_of_lab):
                return map_of_lab
        pos = pos[0] - direction[1][0], pos[1] - direction[1][1]
        return self.fill_map_with_x(map_of_lab, pos, iter_dict)

    def in_range(self, pos, array):
        """Checks if the position is in bounds of the array."""
        rows, cols = array.shape
        row, col = pos
        return bool(0 <= row < rows and 0 <= col < cols)

    def solve_b(self):
        # Brute force: put # in every position, see if it causes infinite loop
        # Don't try this at home, kids!
        count = 0
        map_of_lab = np.array([list(line) for line in self.parsed_data])
        start = np.where(map_of_lab == "^")

        rows, cols = map_of_lab.shape
        for i in range(rows):
            for j in range(cols):
                copied_map = np.copy(map_of_lab)
                copied_map[i, j] = "#"
                try:
                    self.fill_map_with_x(copied_map, start)
                except RecursionError:
                    count += 1
        return count


if __name__ == "__main__":
    current_day = DaySix()
    current_day.print_output()
