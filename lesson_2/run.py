import tweepy
from textblob import TextBlob

consumer_key = 'QGZMMDnmdBG3TI0qX2z8Gh2QO'
consumer_secret = 'K8ODjxgPtlk6tIFz2Wt23xZtsEArFioKavywff55afwpPOV4O0'

access_token = '145992968-akQXNzLuOboxE8iVYazy8XWtTmQ21yxrD0dRJbAP'
access_token_secret = 'Qqiu9vwfXXTFcpXDb4m2fMClH1yljKREll6Z7uheCSx1I'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
  print(tweet.text)
  analysis = TextBlob(tweet.text)
  print(analysis.sentiment)
