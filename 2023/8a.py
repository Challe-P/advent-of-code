""" Solution for 8a """

from itertools import cycle
from aocd import get_data

def data_to_dict(data):
    """Turns the data to a dictionary"""
    desert_map = {}
    for piece in data:
        piece = piece.split()
        desert_map.update({piece[0]: (piece[2][1:4], piece[3][:-1])})
    return desert_map


def main():
    """Main function for 8a"""
    data = get_data(day=8, year=2023).split("\n")
    instructions = data[0]
    instructions = instructions.replace("L", "0")
    instructions = instructions.replace("R", "1")
    instructions = list(map(int, *[instructions]))
    data = data[2:]
    desert_map = data_to_dict(data)
    position = "AAA"
    total_steps = 0
    for instruction in cycle(instructions):
        if position == "ZZZ":
            break
        next_step = instruction
        position = desert_map[position][next_step]
        total_steps += 1
    print(total_steps)

if __name__ == "__main__":
    main()
