import tweepy
from tweepy import OAuthHandler
from twitter import get_auth, twitter_api 

api = twitter_api()

auth = get_auth()

api = tweepy.API(auth)

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