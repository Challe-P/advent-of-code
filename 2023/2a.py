""" Solution for 2a """

from aocd import get_data

def main():
    """ Main function for day 2a of 2023 """
    data = get_data(day=2, year=2023).split("\n")
    max_red = 12
    max_green = 13
    max_blue = 14
    possible_or_not = {}
    game_number = 1
    for game in data:
        game = game.split(":")[1].split(";")
        possible_or_not.update({game_number: True})
        for pull in game:
            if possible_or_not[game_number]:
                pull = pull.split(",")
                for balls in pull:
                    balls = balls.split()
                    if balls[1] == "red" and int(balls[0]) > max_red:
                        possible_or_not.update({game_number: False})
                        break
                    if balls[1] == "green" and int(balls[0]) > max_green:
                        possible_or_not.update({game_number: False})
                        break
                    if balls[1] == "blue" and int(balls[0]) > max_blue:
                        possible_or_not.update({game_number: False})
                        break
        game_number += 1
    sum_of_games = 0
    for result in possible_or_not.items():
        if result[1]:
            sum_of_games += result[0]
    print(sum_of_games)

if __name__ == "__main__":
    main()
