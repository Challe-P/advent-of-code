""" Solution for 2b """
from aocd import get_data

def main():
    """Main function for day 2b of 2023"""
    data = get_data(day=2, year=2023).split("\n")
    sum_of_powers = 0
    game_number = 1
    for game in data:
        max_red = 0
        max_green = 0
        max_blue = 0
        game = game.split(":")[1].split(";")
        for pull in game:
            pull = pull.split(",")
            for balls in pull:
                balls = balls.split()
                if balls[1] == "red":
                    if int(balls[0]) > max_red:
                        max_red = int(balls[0])
                elif balls[1] == "green":
                    if int(balls[0]) > max_green:
                        max_green = int(balls[0])
                elif balls[1] == "blue":
                    if int(balls[0]) > max_blue:
                        max_blue = int(balls[0])
        sum_of_powers += max_red * max_green * max_blue
        game_number += 1
    print(sum_of_powers)

if __name__ == "__main__":
    main()
