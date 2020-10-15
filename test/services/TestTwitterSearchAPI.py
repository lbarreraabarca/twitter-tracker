import unittest
import os
from src.services.TwitterSearchAPI import TwitterSearchAPI
from src.utils.logger import logging

LOG = logging.getLogger(__name__)

class TestSearchResults(object):
    def __init__(self,
                 id: int):
        self._id = id
    
    @property
    def id(self):
        return self._id    

class TestTwitterSearchAPI(unittest.TestCase):
    LOG.info('Testing TwitterSearchAPI class.')
    def test_get_max_id(self):
        self.longMessage = True
        LOG.info('Testing get_max_id method.')
        twitter_api = TwitterSearchAPI(api_key=os.environ.get('TW_API_KEY'),
                                       api_secret=os.environ.get('TW_API_SECRET'))
        id_list = [TestSearchResults(id=1307469509071118338),
                   TestSearchResults(id=1307469484152811520),
                   TestSearchResults(id=1307469473637691398),
                   TestSearchResults(id=1307469466268303360)]
        expected = 1307469466268303360
        actual = twitter_api.get_max_id(id_list)
        self.assertEquals(expected, actual)