from jinja2 import FileSystemLoader, Environment
from .logger import logging

LOG = logging.getLogger(__name__)

class Render():

    def __init__(self,
                 template_name: str):
        self._template_directory = 'template/yaml/'
        self._template_name = template_name

    def render_from_template(self, **kwargs):
        loader = FileSystemLoader(self.template_directory)
        env = Environment(loader=loader)
        template = env.get_template(self.template_name)
        return template.render(**kwargs)

    def save_into_file(self, path, filename, data):
        file = open(f'''{path}/{filename}''', "+w")
        file.write(data)
        file.close()

    @property
    def template_directory(self):
        return self._template_directory

    @property
    def template_name(self):
        return self._template_name
