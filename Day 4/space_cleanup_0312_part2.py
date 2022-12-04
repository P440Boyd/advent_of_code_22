from typing import Tuple
from read_input import read_input_from_daynum


def build_sectors(line: str):
    return line.strip().split(",")


def convert_to_int_list(sector):
    sector_range_int = sector.split("-")
    start, end = int(sector_range_int[0]), int(sector_range_int[1]) + 1
    return list(range(start, end))


def derive_overlap(sectors: Tuple):
    sectors_1, sectors_2 = sectors
    sector_1_nums = convert_to_int_list(sectors_1)
    sector_2_nums = convert_to_int_list(sectors_2)
    if range(
        max(sector_1_nums[0], sector_2_nums[0]),
        min(sector_1_nums[-1], sector_2_nums[-1]) + 1,
    ):
        return True
    return False


def main():
    counter = 0
    puzzle_input = read_input_from_daynum(4)
    for line in puzzle_input:
        sector_tuple = build_sectors(line)
        if derive_overlap(sector_tuple):
            print(f"Found overlap in {line}!")
            counter += 1
    print(f"Total overlap count for all sectors: {counter}.")


if __name__ == "__main__":
    main()
