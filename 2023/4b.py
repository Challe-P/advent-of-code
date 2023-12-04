""" Solution for 4b """

from aocd import get_data

def main():
    """ Main function for day 4b of 2023 """
    data = get_data(day=4, year=2023).split("\n")
    extra_cards = list(range(1, len(data)+1))
    for card, line in enumerate(data, 1):
        winning_numbers, card_numbers = line.split("|")
        winning_numbers = winning_numbers.split(":")[1].split()
        card_numbers = card_numbers.split()
        for i in range(extra_cards.count(card)):
            wins = 0
            for number in winning_numbers:
                wins += card_numbers.count(number)
            for i in range(1, wins+1):
                extra_cards.append(card+i)
    print(len(extra_cards))
    total_cards = [card for card in extra_cards if card <= len(data)+1]
    print(len(total_cards))

if __name__ == "__main__":
    main()
