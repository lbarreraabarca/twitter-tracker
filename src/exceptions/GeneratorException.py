

class GeneratorException(Exception):
    def __init__(self, *args):
        if args:
            self._message = args[0]
        else:
            self._message = None

    def __str__(self):
        if self._message:
            return f'{self._message}'
        else:
            return ''
