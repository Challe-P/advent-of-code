""" Solution for 4a """

from aocd import get_data

def main():
    """ Main function for day 4a of 2023 """
    data = get_data(day=4, year=2023).split("\n")
    total = 0
    for line in data:
        wins = 0
        winning_numbers, card_numbers = line.split("|")
        winning_numbers = winning_numbers.split(":")[1].split()
        card_numbers = card_numbers.split()

        for number in winning_numbers:
            wins += card_numbers.count(number)
        if wins:
            total += 2**(wins-1)
    print(total)


if __name__ == "__main__":
    main()
