from calendar import c
from turtle import pu
from read_input import read_input_from_daynum
import string


def build_ascii_maps():
    ascii_map = {char: pos + 1 for pos, char in enumerate(string.ascii_lowercase)}
    for pos, char in enumerate(string.ascii_uppercase):
        ascii_map[char] = pos + 27
    return ascii_map


def build_groups(puzzle_input):
    counter = 0
    groups = []
    group = []
    for line in puzzle_input:
        if counter < 3:
            group.append(line.strip())
            counter += 1
        else:
            groups.append(group)
            group = [line.strip()]
            counter = 1
    groups.append(group)
    return groups


def main():
    puzzle_input = read_input_from_daynum(3)
    ascii_map = build_ascii_maps()
    total_points = 0
    elf_groups = build_groups(puzzle_input)
    for group in elf_groups:
        common_char = set(group[0]) & set(group[1]) & set(group[2])
        try:
            points_for_char = ascii_map[list(common_char)[0]]
        except IndexError:
            print("Group has no common")
        total_points += points_for_char
    print(f"Total points for all rucksakes: {total_points}.")


if __name__ == "__main__":
    main()
