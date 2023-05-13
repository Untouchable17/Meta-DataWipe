
class FileIsNotValid(Exception):
    def __init__(self, file, message):
        self.file = file
        self.message = message
        super().__init__(self.message)


class InvalidOptionError(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidFileTypeError(Exception):
    def __init__(self, file_type):
        self.file_type = file_type
        super().__init__(f"{file_type} is not a valid file type")

