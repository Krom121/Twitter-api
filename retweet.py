import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

CONSUMER_KEY = 'qljZGMK5DPqwLnDbsmYFlhOAO'
CONSUMER_SECRET = 'ZpngIgEo3MBv6UazZs50hACM0MdUiA2IyRTWoTbAjbieRwwEDO'
OAUTH_TOKEN = '780690706184622080-Pr6M7nCa27eSn4xdGxS3HHT3rvNDSay'
OAUTH_TOKEN_SECRET = 'Utaf5C7Z8pcOPGjSlcsSh9msFYzqFg6hcxdOlvJKLJWM0'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 150
query = 'Ireland'

# Get all the tweets for the search query

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10 #The min amount of retweets

pop_tweets = [status for status in results if status._json['retweet_count'] > min_retweets]

#Create a list of tweet tuples associating each tweet's text with retweet count

tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
                                    for tweet in pop_tweets]

# Sort the tuple entries in decending order

most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

# Pretty Table

table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r'
print(table)