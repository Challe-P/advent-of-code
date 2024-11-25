""" Solution for 8b """
import math
from itertools import cycle
from aocd import get_data

def data_to_dict(data):
    """Turns the data into a dictionary"""
    desert_map = {}
    for piece in data:
        piece = piece.split()
        desert_map.update({piece[0]: (piece[2][1:4], piece[3][:-1])})
    return desert_map

def get_starting_positions(desert_map):
    """Gets the starting positions, that is, all the positions that end with A"""
    positions = []
    for position in desert_map.keys():
        if position[2] == "A":
            positions.append(position)
    return positions

def main():
    """Main function for 8b"""
    data = get_data(day=8, year=2023).split("\n")
    instructions = data[0]
    instructions = instructions.replace("L", "0")
    instructions = instructions.replace("R", "1")
    instructions = list(map(int, *[instructions]))
    data = data[2:]
    desert_map = data_to_dict(data)
    start_positions = get_starting_positions(desert_map)
    total_steps_list = []
    for position in start_positions:
        total_steps = 0
        for instruction in cycle(instructions):
            if position[2] == "Z":
                break
            next_step = instruction
            position = desert_map[position][next_step]
            total_steps += 1
        total_steps_list.append(total_steps)
    least_common_multiple = math.lcm(*total_steps_list)
    print(least_common_multiple)

if __name__ == "__main__":
    main()
