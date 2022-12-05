from typing import List
from read_input import read_input_from_daynum


def get_crate_matrix(puzzle_input: List[str]):
    crate_matrix = []
    for line in puzzle_input:
        if line:
            crate_matrix.append(line)
        else:
            return crate_matrix


def get_puzzle_instructions(puzzle_input: List[str]):
    return puzzle_input[10:]


def return_parsed_instruction(instruction_line: str):
    instruction_line = instruction_line.replace("move", "")
    instruction_line = instruction_line.replace("from", "")
    instruction_line = instruction_line.replace("to", "")
    instruction_line = instruction_line.split()
    return int(instruction_line[0]), int(instruction_line[1]), int(instruction_line[2])


class Stack:
    def __init__(self, items) -> None:
        self.crates: List[str] = self._cleanse(items)

    def _cleanse(self, items):
        return [crate for crate in items if crate != "   "]

    def unstack_crates(self, number_to_unstack):
        target_crates = self.crates[-number_to_unstack:]
        self.crates = self.crates[:-number_to_unstack]
        return target_crates

    def stack_crates(self, crates_to_stack: List[str]):
        # crates_to_stack.reverse()
        self.crates.extend(crates_to_stack)


class CrateMatrix:
    def __init__(self, crate_matrix_list: List[str]) -> None:
        self.input_matrix = crate_matrix_list
        self.rows: List = []
        self.stacks: List = []
        self.height = self._get_stack_height()
        self.column_count = self._get_stack_column_count()
        self._normalise_stacks()
        self._derive_stacks_from_rows()

    def _get_stack_height(self):
        return len(self.input_matrix) - 1

    def _get_stack_column_count(self):
        return len(self.input_matrix[-1].replace(" ", ""))

    def _normalise_stacks(self):
        for row in self.input_matrix[:-1]:
            row_crates = []
            pos_lower = 0
            pos_upper = 3
            for _ in range(self.column_count):
                row_crates.append(row[pos_lower:pos_upper])
                pos_lower += 4
                pos_upper += 4
            for char in row_crates:
                if char == "":
                    row_crates[row_crates.index(char)] = "   "
            self.rows.append(row_crates)

    def _derive_stacks_from_rows(self):
        stack = []
        for i in range(self.column_count):
            for row in self.rows:
                stack.append(row[i])
            stack.reverse()
            self.stacks.append(Stack(stack))
            stack = []

    def move_crates(self, number: int, source: int, destination: int):
        # print(f"Moving {number} crates from stack {source - 1} to {destination -1}.")
        # print(f"{source - 1} before: {self.stacks[source - 1].crates}")
        target_crates = self.stacks[source - 1].unstack_crates(number)
        # print(f"{source - 1} after: {self.stacks[source - 1].crates}")
        # print(f"{destination - 1} before: {self.stacks[destination - 1].crates}")
        self.stacks[destination - 1].stack_crates(target_crates)
        # print(f"{destination - 1} after: {self.stacks[destination - 1].crates}")


def main():
    puzzle_input = read_input_from_daynum(5)
    crate_matrix = get_crate_matrix(puzzle_input)
    puzzle_instructions = get_puzzle_instructions(puzzle_input)
    crates = CrateMatrix(crate_matrix)
    for line in puzzle_instructions:
        number, source, destination = return_parsed_instruction(line)
        crates.move_crates(number, source, destination)
    last_crates = [stack.crates[-1][1] for stack in crates.stacks]
    print(f'Highest crate on each stack: {"".join(last_crates)}')


if __name__ == "__main__":
    main()
