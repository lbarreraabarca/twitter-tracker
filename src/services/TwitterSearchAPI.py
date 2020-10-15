import jsonpickle
import pandas as pd
import tweepy
from src.utils.logger import logging
from src.utils.CommandLine import CommandLine


LOG = logging.getLogger(__name__)

class TwitterSearchAPI():

    def __init__(self,
                 api_key: str,
                 api_secret: str):
        self._api_key = api_key
        self._api_secret = api_secret
        self._authorized = None
        self._api = None

    def connect(self):
        self._authorized = tweepy.AppAuthHandler(self.api_key,
                                                 self.api_secret)
        self._api = tweepy.API(self.authorized,
                               wait_on_rate_limit=True,
                               wait_on_rate_limit_notify=True,
                               retry_count=2)

    def get_tweets(self,
                   search_query: str,
                   lang: str,
                   date: str,
                   max_tweets: int = 1e7,
                   tweets_batch: int = 1e4):
        since_id : int = None
        max_id : int = None
        tweet_count : int = 0

        max_id = self.get_seek(search_query,
                               lang,
                               date)
        since_id : int = max_id - tweets_batch

        while tweet_count < max_tweets:
            tweets = self.api.search(q=search_query,
                                     lang=lang,
                                     until=date,
                                     count=tweets_batch,
                                     since_id=since_id,
                                     max_id=max_id)
            print('len : ', len(tweets))
            if len(tweets) == 0:
                break
            tweet_count += len(tweets)
            since_id = since_id - tweets_batch
            max_id = max_id - tweets_batch
            print(since_id, '...', max_id )
            self.get_tweet_data(tweets)

    def get_tweet_data(self,
                       tweet_list: list):
        for tweet in tweet_list:
            tweet_json = tweet._json
            self.get_tweet_message(tweet_json=tweet_json)
            exit()

    def get_tweet_message(self,
                          tweet_json: dict):
        print(tweet_json['created_at'])
        print(tweet_json['id'])
        print(tweet_json['text'])
        print(tweet_json['truncated'])
        print(tweet_json['source'])
        print(tweet_json['in_reply_to_status_id'])
        print(tweet_json['in_reply_to_user_id'])
        print(tweet_json['in_reply_to_screen_name'])
        print(tweet_json['user']['id'])

    def get_user_data(self,
                      tweet_json: dict):
        print(tweet_json['user']['name'])
        print(tweet_json['user']['screen_name'])
        print(tweet_json['user']['location'])
        print(tweet_json['user']['description'])
        print(tweet_json['user']['followers_count'])
        print(tweet_json['user']['listed_count'])
        print(tweet_json['user']['created_at'])
        print(tweet_json['user']['favourites_count'])
        print(tweet_json['user']['utc_offset'])
        print(tweet_json['user']['time_zone'])
        print(tweet_json['user']['geo_enabled'])
        print(tweet_json['user']['verified'])
        print(tweet_json['user']['statuses_count'])
        print(tweet_json['user']['lang'])
        print(tweet_json['user']['contributors_enabled'])
        print(tweet_json['user']['is_translator'])

    def get_seek(self,
                 search_query: str,
                 lang: str,
                 date: str):
        tweets = self.api.search(q=search_query,
                                 lang=lang,
                                 until=date,
                                 count=1e4,
                                 result_type='recent')
        print(type(tweets))
        return self.get_max_id(tweets)

    def get_max_id(self,
                   tweet_list: list):
        max_id: int = None
        for tweet in tweet_list:
            if max_id is None or max_id < int(tweet.id):
                max_id = int(tweet.id)
        return max_id

    @property
    def api_key(self):
        return self._api_key

    @property
    def api_secret(self):
        return self._api_secret

    @property
    def authorized(self):
        return self._authorized

    @property
    def api(self):
        return self._api
