import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'qljZGMK5DPqwLnDbsmYFlhOAO'
CONSUMER_SECRET = 'ZpngIgEo3MBv6UazZs50hACM0MdUiA2IyRTWoTbAjbieRwwEDO'
OAUTH_TOKEN = '780690706184622080-Pr6M7nCa27eSn4xdGxS3HHT3rvNDSay'
OAUTH_TOKEN_SECRET = 'Utaf5C7Z8pcOPGjSlcsSh9msFYzqFg6hcxdOlvJKLJWM0'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

user = api.get_user('@BarackObama')

print(user.screen_name)
print(user.followers_count)

for friend in user.friends():
    print(friend.screen_name)
    print(friend.followers_count)


# User timeline

for status in tweepy.Cursor(api.home_timeline).items(10):
    #Process a tweet
    print(status.text)