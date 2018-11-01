import json
import tweepy
from tweepy import OAuthHandler
from twitter import get_auth, twitter_api 

api = twitter_api()

auth = get_auth()

api = tweepy.API(auth)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418
MAN_WOE_ID = 28218

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
man_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']
                    for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                    for trend in lon_trends[0]['trends']])

man_trends_set = set([trend['name']
                    for trend in man_trends[0]['trends']])                  

common_trends = set.intersection(dub_trends_set, lon_trends_set, man_trends_set)

print(common_trends)