""" Solution for 7a """
from aocd import get_data

def two_pair_checker(hand):
    """ Checks if the hand is a two pair or a three of a kind. """
    for card in hand:
        copies = hand.count(card)
        if copies == 3:
            return 4
    return 3

def full_house_checker(hand):
    """ Checks if the hand is a full house or four of a kind. """
    for card in hand:
        copies = hand.count(card)
        if copies == 3:
            return 5
    return 6

def strength_checker(hand):
    """ Checks the strength of the hand. """
    hand_set = set(hand)
    match len(hand_set):
        case 5:
            return 1
        case 4:
            return 2
        case 3:
            return two_pair_checker(hand)
        case 2:
            return full_house_checker(hand)
        case 1:
            return 7

def dict_maker(data):
    """ Checks the strength, via a helper function, of all hands and returns them in a dict."""
    scores = {}
    for play in data:
        hand, bet = play.split()
        strength = strength_checker(hand)
        scores.update({hand: [int(bet), strength]})
    return scores

def main():
    """Main function for 7a"""
    test_data= """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    data = test_data.split("\n")
    data = get_data(day=7, year=2023).split("\n")
    sort_order = {"A": 12, "K": 11, "Q": 10, "J": 9,
                  "T": 8, "9": 7, "8": 6, "7": 5, "6": 4,
                   "5": 3, "4": 2, "3": 1, "2": 0}
    scores = dict_maker(data)
    sorted_scores = sorted(
        scores.items(),
        key=lambda x: (
            x[1][1],
            *[sort_order.get(char) for char in x[0] for char in char]
            )
        )
    total_score = 0
    for rank, score in enumerate(sorted_scores, 1):
        total_score += score[1][0] * rank

    print(total_score)

if __name__ == "__main__":
    main()
