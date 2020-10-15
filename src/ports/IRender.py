
from abc import ABCMeta, abstractmethod


class IRender(metaclass=ABCMeta):

    @abstractmethod
    def render(self, template_file, replacement_values):
        raise NotImplementedError
