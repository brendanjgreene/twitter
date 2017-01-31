import tweepy
from tweepy import OAuthHandler
from settings import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN_SECRET, OAUTH_TOKEN

# i have my keys and oauths to a settungs file for privacy

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

user = api.get_user('@madonna')

print user.screen_name
print user.followers_count

for friend in user.friends():
    print
    print friend.screen_name
    print friend.followers_count


