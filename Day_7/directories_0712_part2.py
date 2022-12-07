from logging import root
from Day_7.Directory import Directory
from Day_7.File import File
from read_input import read_input_from_daynum


def evaluate_file(cwd: Directory, file_line: str):
    if file_line.split()[0].isnumeric():
        return File(cwd, file_line.split()[1], int(file_line.split()[0]))


def main():
    puzzle_input = read_input_from_daynum(7)
    root_dir = Directory("/")
    cwd = None
    seen_directories = [root_dir]
    for line in puzzle_input:
        if line.startswith("$ cd"):
            target = line.split()[-1]
            match target:
                case "/":
                    cwd = root_dir
                case "..":
                    cwd = cwd.parent
                case other:
                    new_dir = Directory(target)
                    new_dir.add_parent(cwd)
                    seen_directories.append(new_dir)
                    cwd.add_child(new_dir)
                    cwd = new_dir
        elif line == "$ ls":
            continue
        else:
            if line.split()[0] == "dir":
                continue
            else:
                cwd.add_file(evaluate_file(cwd, line))

    cwd = root_dir
    queue = [root_dir]
    for directory in queue:
        if directory.children not in queue:
            queue.extend(directory.children)
    queue.reverse()
    for directory in queue:
        directory.generate_dir_total_size()

    size_free = 70000000 - cwd.total_size
    smallest = 70000000
    for d in queue:
        if size_free + d.total_size >= 30000000:
            smallest = d
    print(
        f"Found potential directory for deletion: {smallest.name, smallest.total_size}."
    )


if __name__ == "__main__":
    main()
