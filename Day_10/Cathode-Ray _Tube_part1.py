from read_input import read_input_from_daynum


def get_input(file_name):
    with open(file_name, "r") as f:
        data = f.read().splitlines()
    return data


def part_one(data):
    num_stream = get_num_stream(data)
    return sig_strengths(num_stream)


def sig_strengths(num_stream):
    return sum(
        (signal + 1) * num_stream[signal] for signal in range(19, len(num_stream), 40)
    )


def get_num_stream(data):
    data_stream_x = []
    num_x = 1
    for instruction in data:
        data_stream_x.append(num_x)
        if "noop" not in instruction:
            data_stream_x.append(num_x)
            num = int(instruction.split()[-1])
            num_x += num
    return data_stream_x


def part_two(data):
    num_stream = get_num_stream(data)
    display = get_hash_locations(num_stream)
    print_screen(display)
    return "'Check above in the output screen.'"


def get_hash_locations(num_stream):
    crt_screen = ["." for _ in range(240)]
    screen_width = 40
    for location, number in enumerate(num_stream):
        column = location % screen_width
        window_to_search = [column - 1, column, column + 1]
        if number in window_to_search:
            crt_screen[location] = "#"
    return crt_screen


def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


def print_screen(crt_screen):
    screen_width = 40
    for line in chunker(crt_screen, screen_width):
        print(" ".join(line))


def main():
    data = read_input_from_daynum(10)
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")


if __name__ == "__main__":
    main()
