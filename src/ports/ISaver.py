from abc import ABCMeta, abstractmethod


class ISaver(metaclass=ABCMeta):

    @abstractmethod
    def save_file(self, file_path):
        raise NotImplementedError
