from read_input import read_input_from_daynum
import ast


def get_groups(seq):
    data = []
    for line in seq:
        if line == "":
            yield data
            data = []
        else:
            data.append(line)


def normalise_l_r(left, right):
    if isinstance(left, int):
        left = [left]
    elif isinstance(right, int):
        right = [right]
    return left, right


def evaluate_l_r_bool(left, right):
    if left < right:
        return True
    elif left > right:
        return False
    else:
        return None


def correct_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return evaluate_l_r_bool(left, right)
    left, right = normalise_l_r(left, right)
    for l, r in zip(left, right):
        correct = correct_order(l, r)
        if isinstance(correct, bool):
            return correct
    return evaluate_l_r_bool(len(left), len(right))


def part_1(puzzle_input):
    correct = []
    for group_index, group in enumerate(get_groups(puzzle_input), start=1):
        left, right = ast.literal_eval(group[0]), ast.literal_eval(group[1])
        if correct_order(left, right):
            correct.append(group_index)
    print(f"Sum of correct ordered packet indices is {sum(correct)}.")


def part_2(puzzle_input):
    no_space_packets = [ast.literal_eval(line) for line in puzzle_input if line]
    no_space_packets.extend(([[2]], [[6]]))
    ordered = False
    while not ordered:
        ordered = True
        for i in range(len(no_space_packets) - 1):
            if correct_order(no_space_packets[i], no_space_packets[i + 1]) is False:
                holding_item = no_space_packets[i]
                no_space_packets[i] = no_space_packets[i + 1]
                no_space_packets[i + 1] = holding_item
                ordered = False
    print(
        f"Indexes two and six multiplied: {(no_space_packets.index([[2]]) + 1) * (no_space_packets.index([[6]]) + 1)}."
    )


def main():
    puzzle_input = read_input_from_daynum(13)
    part_1(puzzle_input)
    part_2(puzzle_input)


if __name__ == "__main__":
    main()
