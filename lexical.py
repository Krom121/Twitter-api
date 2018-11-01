import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable

CONSUMER_KEY = 'qljZGMK5DPqwLnDbsmYFlhOAO'
CONSUMER_SECRET = 'ZpngIgEo3MBv6UazZs50hACM0MdUiA2IyRTWoTbAjbieRwwEDO'
OAUTH_TOKEN = '780690706184622080-Pr6M7nCa27eSn4xdGxS3HHT3rvNDSay'
OAUTH_TOKEN_SECRET = 'Utaf5C7Z8pcOPGjSlcsSh9msFYzqFg6hcxdOlvJKLJWM0'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 50
query = 'Weather'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count) ]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name'] for status in results for mention in status._json['entities']['user_mentions'] ]

hashtags = [hashtag for status in results for hashtag in status._json['entities']['user_mentions'] ]

words = [word for text in status_texts for word in text.split() ]

for label, data in (('Text', status_texts), ('Screen Name', screen_names), ('Word', words)):
    table = PrettyTable(field_names=[label, 'Count'])
    counter = Counter(data)
    [table.add_row(entry) for entry in counter.most_common()[:10]]
    table.align[label], table.align['Count'] = 'l', 'r'
    print(table)


def get_lexical_diversity(items):
    return 1.0*len(set(items))/len(items)

def get_average_words(tweets):
    total_words = sum([len(tweet.split()) for tweet in tweets])
    return 1.0*total_words/len(tweets)

print("Average Words: {0}".format(get_average_words(status_texts)))
print("Word Diversity: {0}".format(get_lexical_diversity(words)))
print("Screen Name Diversity: {0}".format(get_lexical_diversity(screen_names)))
print("Hashtag Diversity: {0}".format(get_lexical_diversity(hashtags)))  