"""Solves the puzzles for day four 2024"""

from utils import day


class DayFour(day.Day):
    """Solves the puzzles for day four 2024"""

    def __init__(self, year=2024, date=4, data=None):
        super().__init__(year, date, data)

    def solve_a(self):
        total = 0
        for lineindex, line in enumerate(self.parsed_data):
            for index, letter in enumerate(line):
                if letter == "X":
                    total += self.check_neighbours([lineindex, index], "M")

        return total

    def check_neighbours(self, position, letter):
        """Checks X:s neighbours for M, then if AS is there as well"""
        neighbours = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]
        count = 0
        for direction in neighbours:
            matches = {tuple(position): "X"}
            try:
                cur_pos = [
                    position[0] + direction[0],
                    position[1] + direction[1],
                ]
                if cur_pos[0] < 0 or cur_pos[1] < 0:
                    continue
                current_neighbour = self.parsed_data[cur_pos[0]][cur_pos[1]]
                if current_neighbour == letter:
                    matches.update({tuple(cur_pos): "M"})
                    if self.check_direction(cur_pos, "AS", direction):
                        count += 1
            except IndexError:
                continue
        return count

    def check_direction(self, position, letters, direction):
        """Checks for A and S in the direction provided"""
        for char in letters:
            if position[0] + direction[0] < 0 or position[1] + direction[1] < 0:
                return False
            current_char = self.parsed_data[position[0] + direction[0]][
                position[1] + direction[1]
            ]
            if not current_char == char:
                return False
            direction[0] += direction[0]
            direction[1] += direction[1]
        return True

    def solve_b(self):
        total = 0
        for lineindex, line in enumerate(self.parsed_data):
            for index, letter in enumerate(line):
                if letter == "A":
                    total += self.check_diagonals([lineindex, index])
        return total

    def check_diagonals(self, position):
        """Checks the corners around the position if the words spell MAS or SAM"""
        if position[0] < 1 or position[1] < 1:
            return 0
        letters = []
        try:
            nw_letter = self.parsed_data[position[0] - 1][position[1] - 1]
            ne_letter = self.parsed_data[position[0] - 1][position[1] + 1]
            sw_letter = self.parsed_data[position[0] + 1][position[1] - 1]
            se_letter = self.parsed_data[position[0] + 1][position[1] + 1]
            letters.append(nw_letter)
            letters.append(ne_letter)
            letters.append(sw_letter)
            letters.append(se_letter)
        except IndexError:
            return 0
        word_one = letters[0] + "A" + letters[3]
        word_two = letters[1] + "A" + letters[2]
        if word_one not in ("SAM", "MAS") or word_two not in ("SAM", "MAS"):
            return 0
        return 1


if __name__ == "__main__":
    current_day = DayFour()
    current_day.print_output()
