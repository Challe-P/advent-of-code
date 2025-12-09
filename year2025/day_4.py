"""Solves the puzzles for day 4 2025"""

from utils import day


class DayFour(day.Day):
    """Solves the puzzles for day 4 2025"""

    def __init__(self, year=2025, date=4, data=None):
        super().__init__(year, date, data)

    def solve_a(self):
        total = 0
        for lineindex, line in enumerate(self.parsed_data):
            for index, symbol in enumerate(line):
                if symbol == "@":
                    total += self.check_neighbours([lineindex, index], "@")
        return total

    def solve_b(self):
        total = self.remove_rolls(0, self.parsed_data)
        return total

    def remove_rolls(self, total, room_map):
        """Removes rolls from map"""
        old_map = room_map.copy()
        for lineindex, line in enumerate(room_map):
            for index, symbol in enumerate(line):
                if symbol == "@":
                    if self.check_neighbours([lineindex, index], "@") == 1:
                        total += 1
                        line = line[:index] + "." + line[index + 1 :]
                        room_map[lineindex] = line
        if old_map == room_map:
            return total
        return self.remove_rolls(total, room_map)

    def check_neighbours(self, position, letter):
        """Checks X:s neighbours for letter"""
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
            try:
                cur_pos = [
                    position[0] + direction[0],
                    position[1] + direction[1],
                ]
                if cur_pos[0] < 0 or cur_pos[1] < 0:
                    continue
                current_neighbour = self.parsed_data[cur_pos[0]][cur_pos[1]]
                if current_neighbour == letter:
                    count += 1
            except IndexError:
                continue
            if count > 3:
                return 0
        return 1

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


if __name__ == "__main__":
    current_day = DayFour()
    current_day.print_output()
