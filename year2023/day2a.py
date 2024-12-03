"""Solution for 2a"""

import aocd


def main():
    """Main function for day 2a of 2023"""
    data = aocd.get_data(day=2, year=2023).split("\n")
    max_colors = {"red": 12, "green": 13, "blue": 14}
    possible_or_not = {}
    game_number = 1
    for game in data:
        game = game.split(":")[1].split(";")
        possible_or_not.update({game_number: True})
        for pull in game:
            if possible_or_not[game_number]:
                pull = pull.split(",")
                ball_pull(pull, game_number, possible_or_not, max_colors)
        game_number += 1
    sum_of_games = 0
    for result in possible_or_not.items():
        if result[1]:
            sum_of_games += result[0]
    print(sum_of_games)


def ball_pull(pull, game_number, possible_or_not, max_colors):
    """Checks what color the ball is and acts accordingly"""
    for balls in pull:
        balls = balls.split()
        if balls[1] == "red" and int(balls[0]) > max_colors["red"]:
            possible_or_not.update({game_number: False})
            return possible_or_not
        if balls[1] == "green" and int(balls[0]) > max_colors["green"]:
            possible_or_not.update({game_number: False})
            return possible_or_not
        if balls[1] == "blue" and int(balls[0]) > max_colors["blue"]:
            possible_or_not.update({game_number: False})
            return possible_or_not
    return possible_or_not


if __name__ == "__main__":
    main()
