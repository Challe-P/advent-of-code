""" Solution for 9a """
from aocd import get_data

def main():
    """Main function for 9a"""
    data = get_data(day=9, year=2023).split("\n")
    total = []
    for line in data:
        row = list(map(int, line.split()))
        differences = []
        differences.append(row)
        while not all(elements == 0 for elements in differences[-1]):
            row = []
            index = 0
            for index, number in enumerate(differences[-1]):
                if index != 0:
                    row.append(number - differences[-1][index-1])
            differences.append(row)
        differences.reverse()
        for index, row in enumerate(differences):
            if index != 0:
                row.append(row[-1] + differences[index-1][-1])
        total.append(differences[-1][-1])
    print(sum(total))

if __name__ == "__main__":
    main()
