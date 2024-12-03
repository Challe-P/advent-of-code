"""Solves the puzzles for day one 2024"""

from utils import day


class DayTwo(day.Day):
    """Solves the puzzles for day one 2024"""

    def __init__(self, year=2024, date=2, data=None):
        super().__init__(year, date, data)

    def solve_a(self):
        safe_levels = 0
        for line in self.parsed_data:
            level_is_safe = self.line_checker(line.split())
            if level_is_safe:
                safe_levels += 1
        return safe_levels

    def inc_or_dec_check(self, level: int, previous_level: int, status: str):
        """Checks if number is increasing or decreasing,
        and returns False if the direction has changed."""
        direction = self.determine_direction(level, previous_level)
        if not status:
            return direction
        if direction == status:
            return direction
        return False

    def determine_direction(self, level: int, previous_level: int):
        """Determines if the number is increasing or decreasing or not moving"""
        if previous_level < level:
            return "increasing"
        if level < previous_level:
            return "decreasing"
        return False

    def line_checker(self, line, lineindex: int = 0, retries: dict = None) -> bool:
        """Checks if a line is safe"""
        previous_level = None
        inc_or_dec = None
        level_is_safe = False
        retries = {} if retries is None else retries
        for index, level in enumerate(line):
            level = int(level)
            if previous_level:
                if abs(level - previous_level) > 3:
                    retries.update({lineindex: self.retry_line_maker(line, index)})
                    level_is_safe = False
                    break
                inc_or_dec = self.inc_or_dec_check(level, previous_level, inc_or_dec)
                if inc_or_dec:
                    level_is_safe = True
                else:
                    retries.update(
                        {lineindex: self.retry_line_maker(line, index, True)}
                    )
                    level_is_safe = False
                    break
            previous_level = level
        return level_is_safe

    def solve_b(self):
        safe_levels = 0
        retries = {}
        retried_ok = {}
        for lineindex, line in enumerate(self.parsed_data):
            level_is_safe = self.line_checker(line.split(), lineindex, retries)
            if level_is_safe:
                retried_ok.update({lineindex: line})
                safe_levels += 1

        for index, lines in retries.items():
            for line in lines:
                level_is_safe = self.line_checker(line)
                if level_is_safe and index not in retried_ok:
                    retried_ok.update({index: line})
                    safe_levels += 1

        return safe_levels

    def retry_line_maker(self, line: list, index: int, direction: bool = False) -> list:
        """Makes lines to retry, by removing current and previous level,
        and first if it's a direction fault"""
        lines = []
        line_without_prev = line[:]
        line_without_prev.pop(index - 1)
        if direction:
            line_without_first = line[:]
            line_without_first.pop(0)
            lines.append(line_without_first)
        line.pop(index)
        lines.append(line)
        lines.append(line_without_prev)
        return lines


if __name__ == "__main__":
    current_day = DayTwo()
    current_day.print_output()
