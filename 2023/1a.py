from aocd import get_data
def main():
    data = get_data(day=1, year=2023).split()
    digits = []
    for line in data:
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
        digits.append(firstDigit + lastDigit)
    digits = [int(i) for i in digits]
    answer = sum(digits)
    print(answer)

if __name__ == "__main__":
    main()
