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
    puzzle_input = read_input_from_daynum(1)
    elves = build_elves(puzzle_input)
    max_calorie = 0
    for elf in elves:
        elf: Elf
        if elf.calorie_count > max_calorie:
            max_calorie = elf.calorie_count
    print(
        f"The elf carrying the highest number of calories has {max_calorie} calories."
    )


if __name__ == "__main__":
    main()
