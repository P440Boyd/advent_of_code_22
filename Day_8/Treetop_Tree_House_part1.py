from read_input import read_input_from_daynum


def main():
    puzzle_input = read_input_from_daynum(8)
    forest_height = len(puzzle_input)
    forest_width = len(puzzle_input[0])
    matrix = []
    for row in puzzle_input:
        chars = [0 for _ in row]
        matrix.append(chars)
    visible_count = len(puzzle_input[0]) * 2 + len(puzzle_input) * 2 - 4
    maximum = 0
    for x in puzzle_input:
        for y in x:

            print(x, y)


if __name__ == "__main__":
    main()
