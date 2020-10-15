import os
from src.ports.IReader import IReader
from src.exceptions.FileException import FileException


class FileReader(IReader):

    def load_file(self, file_path):
        self.validate(file_path)
        try:
            return open(file_path, "r").read()
        except Exception as ex:
            raise FileException(str(ex))

    def validate(self, file_path):
        if file_path is None:
            raise FileException('File Path cannot be null')
        if file_path == '':
            raise FileException('File Path cannot be empty')
        if not os.path.isfile(file_path):
            raise FileException('File does not Exist')
