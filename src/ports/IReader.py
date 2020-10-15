from abc import ABCMeta, abstractmethod


class IReader(metaclass=ABCMeta):

    @abstractmethod
    def load_file(self, file_path):
        raise NotImplementedError
