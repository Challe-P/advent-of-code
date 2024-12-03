"""Solution for 1b"""

import re
import aocd


def number_converter(line):
    """Converts the number words into numbers."""
    number_words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    result_list = []
    for number in number_words:
        result = [i.start() for i in re.finditer(number, line)]
        if result:
            for i in result:
                result_list.append([i, number])
    result_list.sort()
    for thing in result_list:
        line = line[: thing[0]] + number_words[thing[1]] + line[thing[0] + 1 :]
    return line


def main():
    """Main function for day 1b of 2023"""
    data = aocd.get_data(day=1, year=2023).split()
    digits = []
    for line in data:
        line = number_converter(line)
        first_digit = ""
        last_digit = ""
        line = list(line)
        for char in line:
            if char.isnumeric():
                first_digit = char
                break
        line.reverse()
        for char in line:
            if char.isnumeric():
                last_digit = char
                break
        digits.append(str(first_digit) + str(last_digit))
    digits = [int(i) for i in digits]
    answer = sum(digits)
    print(answer)


if __name__ == "__main__":
    main()
