"""Solution for 7b"""

import aocd


def two_pair_checker(hand):
    """Checks if the hand is a two pair or a three of a kind."""
    for card in hand:
        copies = hand.count(card)
        if copies == 3:
            return 4
    return 3


def full_house_checker(hand):
    """Checks if the hand is a full house or four of a kind."""
    for card in hand:
        copies = hand.count(card)
        if copies == 3:
            return 5
    return 6


def strength_checker(hand):
    """Checks the strength of the hand."""
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


def joker_full_house_checker(hand):
    """Checks if the hand with the joker is a full house or a four of a kind"""
    for card in hand:
        copies = hand.count(card)
        if copies == 2:
            return 5
    return 6


def strength_checker_joker_edition(hand):
    """Checks the strength of hands with a joker in them"""
    jokers = hand.count("J")
    hand = hand.replace("J", "")
    hand_set = set(hand)
    match len(hand_set):
        case 4:
            return 2
        case 3:
            return 4
        case 2:
            if jokers == 1:
                return joker_full_house_checker(hand)
            return 6
        case 1:
            return 7
        case 0:
            return 7


def dict_maker(data):
    """Checks the strength, via helper functions, of all hands and returns them in a dict."""
    scores = {}
    for play in data:
        hand, bet = play.split()
        if "J" in hand:
            strength = strength_checker_joker_edition(hand)
        else:
            strength = strength_checker(hand)
        scores.update({hand: [int(bet), strength]})
    return scores


def main():
    """Main function for 7b"""
    data = aocd.get_data(day=7, year=2023).split("\n")
    sort_order = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
        "J": 0,
    }
    scores = dict_maker(data)
    sorted_scores = sorted(
        scores.items(),
        key=lambda x: (
            x[1][1],
            *[sort_order.get(char) for char in x[0] for char in char],
        ),
    )
    total_score = 0
    for rank, score in enumerate(sorted_scores, 1):
        total_score += score[1][0] * rank
    print(total_score)


if __name__ == "__main__":
    main()
