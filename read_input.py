def read_input_from_daynum(day_number):
    with open(f"input_files/Day {day_number}.txt", "r") as input_fp:
        input_lines = input_fp.readlines()
        return [line.strip() for line in input_lines]
