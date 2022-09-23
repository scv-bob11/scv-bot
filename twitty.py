import json
import logging
import  pprint
import datetime
import requests
from copy import copy

import pytz
import tweepy
from dateutil import parser as date_parser

from env.keys_and_tokens import *

from discord import SyncWebhook


webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1021383709926113331/JoPtrama4TnJUnoauw5nznr4NKJzOWSUjcxOZ84HW4FONvNVCOa7lxnU51zWw25myxxi")


class StreamingTwitter(tweepy.StreamingClient):
    def __init__(self, bearer_token):
        super().__init__(bearer_token)
        webhook.send('The bot is running!')

    
    def structure_tweet(self, data, includes):
        t_t = dict()
        t_t['id'] = data['id']
        t_t['created_at'] = date_parser.parse(data['created_at']).astimezone(pytz.timezone('Asia/Seoul'))
        t_t['text'] = data['text']
        t_t['user'] = includes['users'][0]['name']
        t_t['uid'] = includes['users'][0]['id']
        t_t['profile_image_url'] = includes['users'][0]['profile_image_url']
        t_t['followers'] = includes['users'][0]['public_metrics']['followers_count']
        t_t['url'] = f"https://twitter.com/{includes['users'][0]['username']}/status/{data['id']}"
        return t_t

    def on_data(self, status):
        try:
            status = json.loads(status)
            t_t = self.structure_tweet(status['data'], status['includes'])
            #pprint.pprint(t_t['url'])
            webhook.send(t_t['url'])
        except:
            webhook.send('The bot is dead..')
        


class TwitterBot:
    def __init__(self):
        self.api_key = copy(TWITTER_API_KEY)
        self.api_secret = copy(TWITTER_SECRET)
        self.access_token = copy(TWITTER_ACCESS_TOKEN)
        self.access_secret = copy(TWITTER_ACCESS_SECRET)
        self.bearer_token = copy(TWITTER_BEARER_TOKEN)
        self.twitter_api = self.get_twitter_api()
        self.twitter_client = tweepy.Client(self.bearer_token)
        self.twitter_stream = StreamingTwitter(self.bearer_token)



    def get_twitter_api(self):
        auth = tweepy.OAuth1UserHandler(self.api_key, self.api_secret, self.access_token, self.access_secret)
        return tweepy.API(auth)


    def get_strem(self, stream_listener):
        return tweepy.Stream(self.api_key, self.api_secret, self.access_token, self.access_secret, stream_listener)


    def clear_rules(self):
        ids = list(map(lambda x: x.id, self.twitter_stream.get_rules().data))
        self.twitter_stream.delete_rules(ids)


    def add_rules(self, rule):
        return self.twitter_stream.add_rules(tweepy.StreamRule(rule, tag=''))


    def stream_filter(self):
        return self.twitter_stream.filter(expansions='author_id', tweet_fields=['created_at'], user_fields=['username', 'profile_image_url', 'public_metrics', 'entities'])

