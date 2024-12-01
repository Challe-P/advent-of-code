""" Module for a class with some standard methods and variables for Advent of Code puzzles """
import timeit
import aocd

class Day:
    """ A class with some standard methods and variables for Advent of Code puzzles """
    parsed_data: list
    day: int
    year: int

    def __init__(self, year: int, day: int, data: str = None):
        """ Parses the data and stores in a class variable """
        self.day = day
        self.year = year
        if not data:
            data = aocd.get_data(day=day, year=year)
        self.parsed_data = self.parse_data(data)

    def parse_data(self, data: str) -> list:
        """ Splits data into a list of lines. """
        return data.split("\n")

    def solve_a(self) -> int:
        """ Solves the days first puzzle """
        raise NotImplementedError

    def solve_b(self) -> int:
        """ Solves the days second puzzle """
        raise NotImplementedError

    def solve_performance(self, number=1):
        """ Shows time to run solutions.
        Borrowed from @cave-bjornson (https://github.com/cave-bjornson) """
        results = {}
        try:
            time_a = timeit.Timer(self.solve_a).timeit(number) / number
            results.update({"a": time_a})
        except NotImplementedError:
            results.update({"a": None})
        try:
            time_b = timeit.Timer(self.solve_b).timeit(number) / number
            results.update({"b": time_b})
        except NotImplementedError:
            results.update({"b": None})
        return results

    def print_output(self):
        """ Prints the solutions and a performance result. """
        print("Merry Christmas!")
        print("Running script:\n")
        print(f"Solution for day {self.day}, problem A: {self.solve_a()}\n")
        print(f"Solution for day {self.day}, problem B: {self.solve_b()}\n")
        performance = self.solve_performance(20)
        for solution, time in performance.items():
            if time is None:
                print(f"{solution.upper()} has not been solved yet.")
            if time < 1:
                output = f"\x1b[0;32;40m{time:.3f}\x1b[0m"
            else:
                output = f"\x1b[0;31;40m{time:.3f}\x1b[0m"
            print(f"Average time to solve {solution.upper()}: {output}")
