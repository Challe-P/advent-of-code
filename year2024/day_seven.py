"""Solves the puzzles for day seven 2024"""

import itertools
import operator
from utils import day


class DaySeven(day.Day):
    """Solves the puzzles for day seven 2024"""

    ops = {"+": operator.add, "*": operator.mul, "||": operator.concat}

    def __init__(self, year=2024, date=7, data=None):
        super().__init__(year, date, data)

    def solve_a(self):
        data_dict = self.dict_maker()
        operators = ["+", "*"]
        total = 0
        for key, values in data_dict.items():
            for value in values:
                total += self.check_valid(key, value, operators)
        return total

    def solve_b(self):
        # Takes about 8 seconds, not very good.
        data_dict = self.dict_maker()
        operators = ["+", "*", "||"]
        total = 0
        for key, values in data_dict.items():
            for value in values:
                total += self.check_valid(key, value, operators)
        return total

    def dict_maker(self):
        """Makes a dict from the input with lists of the values associated with the number."""
        res = {}
        for line in self.parsed_data:
            split_line = line.split(": ")
            key = int(split_line[0])
            if key in res:
                res.get(key).append(list(map(int, split_line[1].split(" "))))
            else:
                res.update(
                    {int(split_line[0]): [list(map(int, split_line[1].split(" ")))]}
                )
        return res

    def check_valid(self, key, value, operators):
        """Checks if a row is valid."""
        combs = itertools.product(operators, repeat=len(value) - 1)
        for i in list(combs):
            total = 0
            for index in range(len(value) - 1):
                total = self.check_combination(total, i, value, index)
                if total > key:
                    break
            if total == key:
                return key
        return 0

    def check_combination(self, total, i, value, index):
        """Calculates the number depending on the operator combination."""
        if i[index] == "||":
            if total == 0:
                total = int(
                    self.ops[i[index]](str(value[index]), str(value[index + 1]))
                )
            else:
                total = int(self.ops[i[index]](str(total), str(value[index + 1])))
        else:
            if total == 0:
                total += self.ops[i[index]](value[index], value[index + 1])
            else:
                total = self.ops[i[index]](total, value[index + 1])
        return total


if __name__ == "__main__":
    current_day = DaySeven()
    current_day.print_output()
