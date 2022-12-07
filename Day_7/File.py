class File:
    def __init__(self, directory, filename: str, size: int) -> None:
        self.directory = directory
        self.filename = filename
        self.file_size = size
        self.directory.files_size += size
