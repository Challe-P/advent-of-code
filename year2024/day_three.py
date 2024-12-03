"""Solves the puzzles for day three 2024"""

import re
from utils import day


class DayThree(day.Day):
    """Solves the puzzles for day three 2024"""

    def __init__(self, year=2024, date=3, data=None):
        super().__init__(year, date, data)

    def solve_a(self):
        matches = re.findall(r"mul\((\d*),(\d*)\)", self.unparsed_data)
        total = 0
        for match in matches:
            total += self.mul(int(match[0]), int(match[1]))
        return total

    def mul(self, number, second_number):
        """Elf computing, in real life!"""
        return number * second_number

    def solve_b(self):
        matches = re.findall(
            r"mul\((\d*),(\d*)\)|(do\(\)|don't\(\))", self.unparsed_data
        )
        total = 0
        do = True
        for match in matches:
            if match[2] == "do()":
                do = True
                continue
            if match[2] == "don't()":
                do = False
                continue
            if do:
                total += self.mul(int(match[0]), int(match[1]))
        return total


if __name__ == "__main__":
    current_day = DayThree()
    current_day.print_output()
