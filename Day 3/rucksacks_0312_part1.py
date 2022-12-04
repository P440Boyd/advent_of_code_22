from calendar import c
from read_input import read_input_from_daynum
import string


def build_ascii_maps():
    ascii_map = {char: pos + 1 for pos, char in enumerate(string.ascii_lowercase)}
    for pos, char in enumerate(string.ascii_uppercase):
        ascii_map[char] = pos + 27
    return ascii_map


# def build_rucksacks(puzzle_input):


def main():
    puzzle_input = read_input_from_daynum(3)
    ascii_map = build_ascii_maps()
    total_points = 0
    for line in puzzle_input:
        linechars = list(line.strip())
        midpoint = len(linechars) / 2
        ruck_1 = linechars[: int(midpoint)]
        ruck_2 = linechars[int(midpoint) :]
        common_char = set(ruck_1) & set(ruck_2)
        points_for_char = ascii_map[list(common_char)[0]]
        total_points += points_for_char
    print(f"Total points for all rucksakes: {total_points}.")


if __name__ == "__main__":
    main()
