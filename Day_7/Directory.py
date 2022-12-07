from typing import List
from Day_7.File import File


class Directory:
    def __init__(self, name) -> None:
        self.name = name
        self.children: List[Directory] = []
        self.parent: Directory = None
        self.files: List[File] = []
        self.files_size = 0
        self.total_size = 0

    def _increment_size(self, amount: int):
        self.files_size += amount

    def add_child(self, child_dir_obj):
        self.children.append(child_dir_obj)

    def add_parent(self, parent_name_obj):
        self.parent = parent_name_obj

    def add_file(self, file_obj: File):
        self.files.append(file_obj)
        self._increment_size(file_obj.file_size)

    def generate_dir_total_size(self):
        for file in self.files:
            self.total_size += file.file_size
        for child in self.children:
            self.total_size += child.total_size
