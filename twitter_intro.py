import json
import tweepy
from tweepy import OAuthHandler
from settings import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN_SECRET, OAUTH_TOKEN


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

print common_trends

NYC_WOE_ID = 2459115
BER_WOE_ID = 638242

nyc_trends = api.trends_place(NYC_WOE_ID)
ber_trends = api.trends_place(BER_WOE_ID)

nyc_trends_set = set([trend['name']
                      for trend in nyc_trends[0]['trends']])

ber_trends_set = set([trend['name']
                      for trend in ber_trends[0]['trends']])

foreign_trends = set.intersection(nyc_trends_set, ber_trends_set)

print foreign_trends

dif_trends = set.difference(nyc_trends_set, ber_trends_set)

print dif_trends