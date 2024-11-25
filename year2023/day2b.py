""" Solution for 2b """
import aocd

def main():
    """ Main function for day 2b of 2023 """
    data = aocd.get_data(day=2, year=2023).split("\n")
    sum_of_powers = 0
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
                    max_red = max(max_red, int(balls[0]))
                elif balls[1] == "green":
                    max_green = max(max_green, int(balls[0]))
                elif balls[1] == "blue":
                    max_blue = max(max_blue, int(balls[0]))
        sum_of_powers += max_red * max_green * max_blue
    print(sum_of_powers)

if __name__ == "__main__":
    main()
