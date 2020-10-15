from src.models.AbstractRequest import AbstractRequest
from src.utils.logger import logging

LOG = logging.getLogger(__name__)

class QualityRequest(AbstractRequest):

    ERROR_MESSAGE = "Field Cannot be Empty or Null"

    def __init__(self,
                 twitter_query: str,
                 twitter_lang: str,
                 twitter_date: str,
                 bq_project: str,
                 bq_dataset: str,
                 bq_table: str):
        super().__init__()
        self._twitter_query = twitter_query
        self._twitter_lang = twitter_lang
        self._twitter_date = twitter_date
        self._bq_project = bq_project
        self._bq_dataset = bq_dataset
        self._bq_table = bq_table

    def validate(self):
        if self._twitter_query is None \
                or self._twitter_query == '':
            self.add_error("twitter_query", self.ERROR_MESSAGE)
        if self._bq_project is None \
                or self._bq_project == '':
            self.add_error("bq_project", self.ERROR_MESSAGE)
        if self._bq_dataset is None \
                or self._bq_dataset == '':
            self.add_error("bq_dataset", self.ERROR_MESSAGE)
        if self._bq_table is None \
                or self._bq_table == '':
            self.add_error("bq_table", self.ERROR_MESSAGE)

    @classmethod
    def from_dict(cls, i_dict):
        twitter_query = i_dict['TWITTER']['QUERY'].lower()
        twitter_lang = i_dict['TWITTER']['LANG'].lower()
        twitter_date = i_dict['TWITTER']['DATE'].lower()
        bq_project = i_dict['BIG_QUERY']['PROJECT'].lower()
        bq_dataset = i_dict['BIG_QUERY']['DATASET'].lower()
        bq_table = i_dict['BIG_QUERY']['TABLE'].lower()

        return QualityRequest(twitter_query=twitter_query,
                              twitter_lang=twitter_lang,
                              twitter_date=twitter_date,
                              bq_project=bq_project,
                              bq_dataset=bq_dataset,
                              bq_table=bq_table)

    @property
    def twitter_query(self):
        return self._twitter_query

    @property
    def twitter_lang(self):
        return self._twitter_lang

    @property
    def twitter_date(self):
        return self._twitter_date

    @property
    def bq_project(self):
        return self._bq_project

    @property
    def bq_dataset(self):
        return self._bq_dataset

    @property
    def bq_table(self):
        return self._bq_table
