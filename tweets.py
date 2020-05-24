import config as cfg
import tweepy as tw
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pandas as pd
import csv
import re

#Twitter credentials for the app
consumer_key = cfg.API_Key
consumer_secret = cfg.API_SECRET
access_key= cfg.Access_token
access_secret = cfg.Token_Secret

#pass twitter credentials to tweepy
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tw.API(auth)

# Collect tweets
tweets = tw.Cursor(api.search,
              q=cfg.keyword,
              lang="en",
              since=cfg.date).items(cfg.number_tweets)

data = [[tweet.user.screen_name, tweet.user.location, tweet.text] for tweet in tweets]

tweet_df = pd.DataFrame(data=data, 
                    columns=['user', "location","tweet"])

print(tweet_df)