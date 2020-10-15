from abc import ABCMeta, abstractmethod


class IParser(metaclass=ABCMeta):

    @abstractmethod
    def parse(self, data):
        raise NotImplementedError
