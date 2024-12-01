""" Solves the puzzles for day one 2024 """

from utils import day

class DayOne(day.Day):
    """ Solves the puzzles for day one 2024 """

    def __init__(self, year=2024, date=1, data = None):
        super().__init__(year, date, data)

    def solve_a(self):
        left_list, right_list = self.list_splitter()
        left_list.sort()
        right_list.sort()
        total_distance = 0
        for index, loc_id in enumerate(left_list):
            total_distance += abs(right_list[index] - loc_id)
        return total_distance

    def solve_b(self):
        left_list, right_list = self.list_splitter()
        total_score = 0
        for loc_id in left_list:
            total_score += (loc_id * right_list.count(loc_id))
        return total_score

    def list_splitter(self) -> list[list]:
        """ Splits the parsed input in one left and one right part """
        left_list = []
        right_list = []
        for line in self.parsed_data:
            left_number, right_number = line.split()
            left_list.append(int(left_number))
            right_list.append(int(right_number))
        return left_list, right_list

if __name__ == "__main__":
    current_day = DayOne()
    current_day.print_output()
