"""Solves the puzzles for day five 2024"""

import re
from utils import day


class DayFive(day.Day):
    """Solves the puzzles for day five 2024"""

    rules = []
    rule_dict = []
    lines = []

    def __init__(self, year=2024, date=5, data=None):
        super().__init__(year, date, data)

    def solve_a(self):
        self.five_parser()
        good_lines = []
        for line in self.lines:
            line_ok = True
            numbers = line.split(",")
            numbers = list(numbers)
            for number in numbers:
                line_ok, _ = self.check_number(number, line)
                if not line_ok:
                    break
            if line_ok:
                good_lines.append(line)
        res = 0
        for line in good_lines:
            line = line.split(",")
            index = int((len(line) / 2))
            res += int(line[index])
        return res

    def solve_b(self):
        self.five_parser()
        bad_lines = []
        for line in self.lines:
            numbers = line.split(",")
            numbers = list(numbers)
            for number in numbers:
                line_ok, _ = self.check_number(number, line)
                if not line_ok:
                    bad_lines.append(line)
                    break
        correct_lines = []
        for line in bad_lines:
            correct_lines.append(self.fix_report(line))

        res = 0
        for line in correct_lines:
            line = line.split(",")
            index = int((len(line) / 2))
            res += int(line[index])
        return res

    def fix_report(self, line, line_ok=False):
        """Fixes a line by checking it and moving numbers around"""
        numbers = line.split(",")
        numbers = list(numbers)
        for number in numbers:
            line_ok, broken_rule = self.check_number(number, line)
            if broken_rule:
                rule = broken_rule.split(".*,")
                index = numbers.index(rule[1])
                numbers.remove(rule[0])
                numbers.insert(index, rule[0])
                line = ",".join(numbers)
                return self.fix_report(line, line_ok)
        return line

    def check_number(self, number, line):
        """Checks if a number has a rule and if that rule is broken"""
        res = True
        broken_rule = None
        if number in self.rule_dict.keys():
            for corr in self.rule_dict[number]["corr"]:
                if corr in line:
                    if re.search(self.rule_dict[number][corr], line):
                        res = True
                    else:
                        res = False
                        broken_rule = self.rule_dict[number][corr]
                        break
        return res, broken_rule

    def five_parser(self):
        """Parses the data for day five"""
        index = self.parsed_data.index("")
        self.rules = self.parsed_data[:index]
        unflat_split = [x.split("|") for x in self.rules]
        split_rules = [elem for subl in unflat_split for elem in subl]
        self.rule_dict = {number: {"corr": []} for number in split_rules}
        for rule in self.rules:
            part_one, part_two = rule.split("|")
            regex = part_one + ".*," + part_two
            if part_one in self.rule_dict:
                self.rule_dict[part_one]["corr"].append(part_two)
                self.rule_dict[part_one].update({part_two: regex})
            if part_two in self.rule_dict:
                self.rule_dict[part_two]["corr"].append(part_one)
                self.rule_dict[part_two].update({part_one: regex})

        self.lines = self.parsed_data[index + 1 :]


if __name__ == "__main__":
    current_day = DayFive()
    current_day.print_output()
