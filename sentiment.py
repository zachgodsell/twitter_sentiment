from textblob import TextBlob
import pandas as pd
import tweets as tw

# Creates as dataframe that has the sentiment and polarity for each tweet
def dataframe_sen_pol(df):
    
    # The x in the lambda function is a row (because I set axis=1)
    # Apply iterates the function accross the dataframe's rows
    df['polarity'] = df.apply(lambda x: TextBlob(x['cleaned_tweet']).sentiment.polarity, axis=1)
    df['subjectivity'] = df.apply(lambda x: TextBlob(x['cleaned_tweet']).sentiment.subjectivity, axis=1)

    return df

def avg_polarity(df):
    avg_pol = df['polarity'].mean()
    return avg_pol


def avg_subjectivity(df):
    avg_sub = df['subjectivity'].mean()
    return avg_sub

