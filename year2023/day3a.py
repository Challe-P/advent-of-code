""" Solution for 3a """

from aocd import get_data

def main():
    """ Main function for day 3a of 2023 """
    data = get_data(day=3, year=2023).split()
    valid_numbers = {}
    x = 0
    for row in data:
        y = 0
        for point in row:
            if point != "." and not point.isnumeric():
                neighbours = get_neighbours(x, y)
                valid_numbers = number_validator(neighbours, data, valid_numbers)
            y += 1
        x += 1
    print(sum(valid_numbers.values()))

def get_neighbours(x, y):
    """ Returns the neighbours of the given coordinate in a list """
    neighbours = []
    neighbours.append([[x-1, y-1], [x-1, y], [x-1, y+1],
                       [x, y-1],             [x, y+1],
                       [x+1, y-1], [x+1, y], [x+1, y+1]])
    return neighbours

def number_validator(neighbours, data, valid_numbers):
    """ Checks if the number is valid, and puts it in a dictionary """
    for coordinates_list in neighbours:
        for coordinates in coordinates_list:
            if data[coordinates[0]][coordinates[1]].isnumeric():
                y_coordinate, number = full_number_getter(coordinates[0], coordinates[1], data)
                valid_numbers.update({(coordinates[0], y_coordinate): number})
    return valid_numbers

def full_number_getter(x, y, data):
    """ Checks the line back and forwards to get a complete number """
    full_number = []
    y_down = y
    y_up = y+1
    for _ in data[x]:
        while y_down >= 0 and data[x][y_down].isnumeric():
            full_number.insert(0, data[x][y_down])
            y_coordinate = y_down
            y_down -= 1
        try:
            while y_up <= len(data[x]) and data[x][y_up].isnumeric():
                full_number.append(data[x][y_up])
                y_up += 1
        except IndexError:
            continue

    full_number = "".join(full_number)
    return y_coordinate, int(full_number)

if __name__ == "__main__":
    main()
