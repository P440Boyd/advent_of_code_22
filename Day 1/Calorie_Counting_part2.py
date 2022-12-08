from typing import List
from read_input import read_input_from_daynum


class Elf:
    def __init__(self) -> None:
        self.calorie_count: int = 0

    def add_calories(self, calorie_num):
        self.calorie_count = self.calorie_count + calorie_num


def build_elves(input_data):
    elves = []
    new_elf = Elf()
    for line_content in input_data:
        try:
            int(line_content)
            new_elf.add_calories(int(line_content.strip()))
        except Exception:
            elves.append(new_elf)
            new_elf = Elf()
    return elves


def main():
    calorie_data = read_input_from_daynum(1)
    elves: List[Elf] = build_elves(calorie_data)
    calorie_count_list = [elf.calorie_count for elf in elves]
    calorie_count_list.sort()
    first, second, third = (
        calorie_count_list[-1],
        calorie_count_list[-2],
        calorie_count_list[-3],
    )
    total_top_three = first + second + third
    print(
        f"The elf carrying the highest number of calories has {calorie_count_list[-1]} calories."
    )
    print(f"The top three carried calorie counts are: {first}, {second}, {third}.")
    print(f"The sum of these components is {total_top_three}.")


if __name__ == "__main__":
    main()
