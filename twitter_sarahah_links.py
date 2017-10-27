
# ### Install and import all necessary libraries
# - pip install python-twitter

import twitter
import json
import pandas as pd
import base64
import re

ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_SECRET)
print(api.VerifyCredentials())


def get_tweets(term, count):
 all_tweets = []
 loop_count = count // 100
 for i in range(loop_count):
     tweets = api.GetSearch(term=term, count = 100)
     try:
         all_tweets = all_tweets + tweets
     except:
         print('something wrong')
         pass
 return all_tweets
  

def get_tweets_df(tweets):
 result = []
 for tweet in tweets:
     text = tweet.text
     urls = tweet.urls
     
     result.append({
         'text': text.encode('ascii', 'ignore').decode('ascii'),
         'urls': urls
     })
 result_df = pd.DataFrame(result)
 return result_df



tweets_sarahah_links = get_tweets('sarahah', 1000)

df_tweets_sarahah_links = get_tweets_df(tweets_sarahah_links)

all_links = df_tweets_sarahah_links['urls'].to_string()

regex = r'https://[^\s<>"]+\.sarahah\.com'
ans = re.findall(regex, all_links)

import csv

with open('twitter_sarahah_links.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in ans:
        writer.writerow([val])