def read_input_from_daynum(day_number):
    with open(f"input_files/Day {day_number}.txt", "r") as input_fp:
        return input_fp.readlines()
