from read_input import read_input_from_daynum


def find_unique_msg_end(msg_length: int, puzzle_input: str):
    for i in range(len(puzzle_input)):
        if len(set(puzzle_input[i : i + msg_length])) == msg_length:
            print(
                f"Detected unique string {puzzle_input[i : i + msg_length]}. Visible by character {i+msg_length}."
            )
            break


def main():

    puzzle_input = read_input_from_daynum(6)
    puzzle_input_str = puzzle_input[0]
    find_unique_msg_end(14, puzzle_input_str)


if __name__ == "__main__":
    main()
