def read_input():
    with open("Day 3", "r") as input_fp:
        return input_fp.readlines()


def main():
    puzzle_input = read_input()
    for line in puzzle_input:
        print(line)


if __name__ == "__main__":
    main()
