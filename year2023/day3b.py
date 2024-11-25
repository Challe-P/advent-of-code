""" Solution for 3b """

import aocd

def main():
    """ Main function for day 3b of 2023 """
    data = aocd.get_data(day=3, year=2023).split()

    valid_numbers = {}
    gear_neighbours = {}
    x = 0
    for row in data:
        y = 0
        for point in row:
            if point == "*":
                neighbours = get_neighbours(x, y)
                gear_neighbours.update({(x, y): neighbours})
                valid_numbers = number_validator(neighbours, data, valid_numbers)
            y += 1
        x += 1

    print(gear_checker_3000(valid_numbers, gear_neighbours))

def get_neighbours(x, y):
    """ Returns the neighbours of the given coordinate in a list """
    neighbours = []
    # Weird graphic because it helps visualize what's going on.
    neighbours.append([[x-1, y-1], [x-1, y], [x-1, y+1],
                       [x, y-1],             [x, y+1],
                       [x+1, y-1], [x+1, y], [x+1, y+1]])
    return neighbours

def number_validator(neighbours, data, valid_numbers):
    """ Checks if the number is valid, and puts it in a dictionary """
    for coordinates_list in neighbours:
        for coordinates in coordinates_list:
            if data[coordinates[0]][coordinates[1]].isnumeric():
                coordinates, number = full_number_getter(coordinates[0], coordinates[1], data)
                valid_numbers.update({coordinates: number})
    return valid_numbers

def full_number_getter(x, y, data):
    """ Checks the line back and forwards to get a complete number """
    full_number = []
    coordinates = []
    y_down = y
    y_up = y+1
    for _ in data[x]:
        while y_down >= 0 and data[x][y_down].isnumeric():
            full_number.insert(0, data[x][y_down])
            coordinates.append((x, y_down))
            y_down -= 1
        # Try because it may be out of bounds.
        try:
            while y_up <= len(data[x]) and data[x][y_up].isnumeric():
                full_number.append(data[x][y_up])
                coordinates.append((x, y_up))
                y_up += 1
        except IndexError:
            continue
    coordinates.sort()
    coordinates = tuple(coordinates)
    full_number = "".join(full_number)
    return coordinates, int(full_number)

def gear_checker_3000(valid_numbers, gear_neighbours):
    """ Checks the gear list if the gear symbol (*) is next to exactly two numbers, multiplies
    them and then returns the sum of all the gear numbers. """
    flat_coordinate_list = [item for sublist in valid_numbers.keys() for item in sublist]
    total_numbers = 0
    for neighbour_list_of_lists in gear_neighbours.values():
        numbers = []
        for neighbour_list in neighbour_list_of_lists:
            for neighbour in neighbour_list:
                neighbour = tuple(neighbour)
                if neighbour in flat_coordinate_list:
                    value = next(v for (k,v) in valid_numbers.items() if neighbour in k)
                    if value not in numbers:
                        numbers.append(value)
            if len(numbers) == 2:
                total_numbers += numbers[0] * numbers[1]
    return total_numbers


if __name__ == "__main__":
    main()
