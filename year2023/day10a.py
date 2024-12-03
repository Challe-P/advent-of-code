"""Solution for 10a"""

import sys
import aocd

directions = {
    "north": {"|": (1, 0), "L": (0, 1), "J": (0, -1)},
    "south": {"|": (-1, 0), "7": (0, -1), "F": (0, 1)},
    "east": {"-": (0, -1), "L": (-1, 0), "F": (1, 0)},
    "west": {"-": (0, 1), "J": (-1, 0), "7": (1, 0)},
}

origin = {(1, 0): "north", (-1, 0): "south", (0, 1): "west", (0, -1): "east"}


def main():
    """Main function for 10a"""
    sys.setrecursionlimit(20000)
    datadict, start_point = data_parser()

    # Check the four surrounding pipes - see where the loop is
    direction, point = loop_start_finder(datadict, start_point)

    # Count how many steps until back to S
    count = loop(datadict, point, direction)

    # Print result
    print((count + 1) // 2)


def data_parser():
    """Parses data into dictionary with points as tuple keys"""
    data = aocd.get_data(day=10, year=2023).split("\n")
    start_point = ()
    datadict = {}
    for index, line in enumerate(data):
        for charindex, char in enumerate(line):
            if char == "S":
                start_point = (index, charindex)
            datadict.update({(index, charindex): char})
    return datadict, start_point


def loop_start_finder(datadict, start_point) -> list[tuple]:
    """Checks around the start position for possible loop starts"""
    if direction_checker(datadict, (start_point[0] - 1, start_point[1]), start_point):
        return "south", (start_point[0] - 1, start_point[1])
    if direction_checker(datadict, (start_point[0] + 1, start_point[1]), start_point):
        return "north", (start_point[0] + 1, start_point[1])
    if direction_checker(datadict, (start_point[0], start_point[1] + 1), start_point):
        return "west", (start_point[0], start_point[1] + 1)
    if direction_checker(datadict, (start_point[0], start_point[1] - 1), start_point):
        return "east", (start_point[0], start_point[1] - 1)
    return "no loop"


def direction_checker(datadict: dict, point: tuple, start_point: tuple) -> bool:
    """Checks if the point has an exit to the start"""
    for _, pipe in directions.items():
        if datadict[point] in pipe:
            steps = pipe[datadict[point]]
            if (point[0] + steps[0], point[1] + steps[1]) == start_point:
                return True
    return False


def loop(datadict: dict, point: tuple, previous: str, count: int = 0):
    """Recursive loop for going through the pipes"""
    if datadict[point] == "S":
        return count
    new_point = (
        point[0] + directions[previous][datadict[point]][0],
        point[1] + directions[previous][datadict[point]][1],
    )
    previous = origin[directions[previous][datadict[point]]]
    # Add flag to mark part of loop
    datadict[point] = "\x1b[6;30;42m" + datadict[point] + "\x1b[0m", True
    return loop(datadict, new_point, previous, count + 1)


if __name__ == "__main__":
    main()
