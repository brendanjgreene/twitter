import json
import tweepy
from tweepy import OAuthHandler
from settings import CONSUMER_KEY
from settings import CONSUMER_SECRET
from settings import OAUTH_TOKEN
from settings import OAUTH_TOKEN_SECRET


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

print json.dumps(dub_trends, indent=1)
print json.dumps(lon_trends, indent=1)

