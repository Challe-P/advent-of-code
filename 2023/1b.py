from aocd import get_data
import re

def numberConverter(line):
    number_words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    result_list = []
    for number in number_words.keys():
        result = [i.start() for i in re.finditer(number, line)]
        if result:
            for i in result:
                result_list.append([i, number])
    result_list.sort()
    for thing in result_list:
        line = line[:thing[0]] + number_words[thing[1]] + line[thing[0]+1:]
    return line

def main():
    data = get_data(day=1, year=2023).split()
    digits = []
    new_lines = []
    for line in data:
        # Borde hoppas över om första och sista karaktären är en siffra.
        line = numberConverter(line)
        new_lines.append(line)
        firstDigit = ""
        lastDigit = ""
        line = list(line)
        for char in line:
            if char.isnumeric():
                firstDigit = char
                break
        line.reverse()
        for char in line:
            if char.isnumeric():
               lastDigit = char
               break
        digits.append(str(firstDigit) + str(lastDigit))
    
    digits = [int(i) for i in digits]
    answer = sum(digits)
    print(answer)

if __name__ == "__main__":
    main()

