""" Solution for 4b """
import aocd

def card_dict_maker(data):
    """Turns the data into a dict for faster processing"""
    card_dict = {}

    for card, line in enumerate(data, 1):
        winning_numbers, card_numbers = line.split("|")
        winning_numbers = set(winning_numbers.split(":")[1].split())
        card_numbers = set(card_numbers.split())
        wins = len(winning_numbers.intersection(card_numbers))
        copies = 1
        card_dict.update({card: [wins, copies]})

    return card_dict

def win_checker(card_dict):
    """Simulates the ticket chain reaction"""
    total_copies = 0
    for i in card_dict:
        total_copies += card_dict.get(i)[1]
        for j in range(1, card_dict.get(i)[0]+1):
            card_dict[i+j][1] += 1*card_dict.get(i)[1]
    return total_copies

def main():
    """Main function for 4b"""
    data = aocd.get_data(day=4, year=2023).split("\n")
    #data = test_data.split("\n")
    card_dict = card_dict_maker(data)
    print(win_checker(card_dict))

if __name__ == "__main__":
    main()
