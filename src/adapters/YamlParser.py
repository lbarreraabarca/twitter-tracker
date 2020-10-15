import yaml
from src.ports.IParser import IParser
from src.exceptions.ParserExpection import ParserExpection


class YamlParser(IParser):

    def parse(self, data):
        if data is None:
            raise ParserExpection('Input YAML cannot be null')
        if data == '':
            raise ParserExpection('Input YAML cannot be empty')
        try:
            return self.yaml_to_dict(data)
        except Exception as ex:
            raise ParserExpection(str(ex))

    def yaml_to_dict(self, data):
        try:
            result = yaml.load(data, Loader=yaml.BaseLoader)
            return result
        except Exception:
            raise ParserExpection('Input YAML is invalid')
