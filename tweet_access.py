import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'qljZGMK5DPqwLnDbsmYFlhOAO'
CONSUMER_SECRET = 'ZpngIgEo3MBv6UazZs50hACM0MdUiA2IyRTWoTbAjbieRwwEDO'
OAUTH_TOKEN = '780690706184622080-Pr6M7nCa27eSn4xdGxS3HHT3rvNDSay'
OAUTH_TOKEN_SECRET = 'Utaf5C7Z8pcOPGjSlcsSh9msFYzqFg6hcxdOlvJKLJWM0'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 10
query = 'Dublin'

#Get all status

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

for result in results:
   print(json.dumps(result._json, indent=4))

for status in results:
    print(status.text.encode('utf-8'))
    print(status.user.id)
    print(status.user.screen_name)
    print(status.user.profile_image_url_https)
    print(status.user.followers_count)
    print(status.place) 