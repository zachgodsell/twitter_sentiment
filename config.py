import re
# Twitter Credentials
API_Key = 'QqNQCYCvapfviyDz9rERpU3rT' 
API_SECRET = 'qRyj8XMjb9a4p40TnOXP8s1GLXfKxo8yrnykauxWbtoRjKSsn4'
Access_token = '1264387120510103552-2jiCamfUvOm859w7p8rJoeuWUtkwwY'
Token_Secret = 'C6js0NP4zpPi0rq8H6HnGnLklI8wRF94lLtP4rCBDDODn'

# Search information
keyword = '#AFL'
date = '2020-05-01'
number_tweets = 200


#Types of emojis:

#Happy Emoticons:
emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
    ])

#Sad emoticons:

emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
    ])


#Emoji patterns
emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         "]+", flags=re.UNICODE)


#combine sad and happy emoticons

emoticons = emoticons_happy.union(emoticons_sad)