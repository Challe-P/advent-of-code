# Check each . if it's adjecent to the loop or another . convert to O or I?
# Make a manual check?
import sys
import day10a


def main():
    sys.setrecursionlimit(20000)
    pipe_map, start_point = day10a.data_parser()
    # Check the four surrounding pipes - see where the loop is
    direction, point = day10a.loop_start_finder(pipe_map, start_point)

    # Count how many steps until back to S
    day10a.loop(pipe_map, point, direction)

    pretty_pipes = {
        "\x1b[6;30;42mF\x1b[0m": "\u250f",
        "\x1b[6;30;42m-\x1b[0m": "\u2500",
        "\x1b[6;30;42m7\x1b[0m": "\u2510",
        "\x1b[6;30;42mJ\x1b[0m": "\u2518",
        "\x1b[6;30;42mL\x1b[0m": "\u2514",
        "\x1b[6;30;42m|\x1b[0m": "\u2503",
    }
    count = 0
    table = ""
    for i in range(0, 140):
        row = ""
        for j in range(0, 140):
            if not pipe_map[(i, j)][0].startswith("\x1b[6;30;42m"):
                pipe_map[(i, j)] = "."
            if pipe_map[(i, j)][0] in pretty_pipes:
                pipe_map[(i, j)] = pretty_pipes[pipe_map[(i, j)][0]]
            row += pipe_map[(i, j)][0]
        table += row + "\n"
    print(table)
    print(count)


if __name__ == "__main__":
    main()
