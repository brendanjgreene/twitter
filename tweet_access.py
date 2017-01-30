import json
import tweepy
from tweepy import OAuthHandler
from settings import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN_SECRET, OAUTH_TOKEN

# i have my keys and oauths to a settungs file for privacy

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 10
query = 'Dublin'

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

for result in results:
    print json.dumps(result._json, indent=2)
