from abc import ABCMeta, abstractmethod


class AbstractRequest(metaclass=ABCMeta):

    def __init__(self):
        self.errors = {}

    def is_valid(self):
        self.validate()
        return self.errors == {}

    @abstractmethod
    def validate(self):
        raise NotImplementedError

    def get_errors(self):
        return self.errors

    def add_error(self, field, error):
        self.errors.update({field: error})
