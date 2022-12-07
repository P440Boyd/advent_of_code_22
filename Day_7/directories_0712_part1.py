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
        # queue.pop(queue.index(directory))

    total_size = 0
    for directory in queue:
        if directory.total_size >= 22951914:
            print(
                f"Directory name is {directory.name}. It has children {directory.children} and parent {directory.parent}. Size of files in its directory is {directory.total_size}."
            )
            total_size += directory.total_size

    size_free = 70_000_000 - cwd.total_size

    for d in queue:
        if size_free + d.total_size >= 30000000:
            print(d.name, d.total_size)
            break

    print(f"Size of dirs with files smaller than 100000 is: {total_size}.")


if __name__ == "__main__":
    main()
