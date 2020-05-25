import config as cfg
import tweepy as tw
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pandas as pd
import csv
import re
import preprocessor as p
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
nltk.download('stopwords')





def clean_tweets(tweet):
    
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(tweet)#after tweepy preprocessing the colon symbol left remain after      #removing mentions
    tweet = re.sub(r':', '', tweet)
    tweet = re.sub(r'‚Ä¶', '', tweet)
#replace consecutive non-ASCII characters with a space
    tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)#remove emojis from tweet
    tweet = cfg.emoji_pattern.sub(r'', tweet)#filter using NLTK library append it to a string
    filtered_tweet = [w for w in word_tokens if not w in stop_words]
    filtered_tweet = []#looping through conditions
    for w in word_tokens:
#check tokens against stop words , emoticons and punctuations
        if w not in stop_words and w not in cfg.emoticons and w not in string.punctuation:
            filtered_tweet.append(w)
    return ' '.join(filtered_tweet)






def get_tweet_df():
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

    new_list = []
    for i in data:
        data = clean_tweets(i[2])
        i.append(data)
        new_list.append(i)


    tweet_df = pd.DataFrame(data=new_list, 
                    columns=['user', "location","original_tweet", "cleaned_tweet"])

    return tweet_df
