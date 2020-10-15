import json
from src.utils.logger import logging

LOG = logging.getLogger(__name__)

class View():
    def __init__(self,
                 filename: str):
        self._filename = filename
        self._views_dict = None
        self.create_df()

    def create_df(self):
        self._views_dict = json.loads(open(self.filename, 'r').read())
        self._views_dict = self.views_dict['views']

    @property
    def filename(self):
        return self._filename

    @property
    def views_dict(self):
        return self._views_dict
