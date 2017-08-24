import tweepy
import csv
from textblob import TextBlob

consumer_key = 'QGZMMDnmdBG3TI0qX2z8Gh2QO'
consumer_secret = 'K8ODjxgPtlk6tIFz2Wt23xZtsEArFioKavywff55afwpPOV4O0'

access_token = '145992968-akQXNzLuOboxE8iVYazy8XWtTmQ21yxrD0dRJbAP'
access_token_secret = 'Qqiu9vwfXXTFcpXDb4m2fMClH1yljKREll6Z7uheCSx1I'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

topic = input('What is your topic? ')
public_tweets = api.search(topic)

labeled = []

for tweet in public_tweets:
  analysis = TextBlob(tweet.text)
  polarity = ''
  if analysis.sentiment.polarity >= 0:
    polarity = 'positive'
  else:
    polarity = 'negative'
  labeled.append({'text': tweet.text.encode("utf-8"), 'polarity': polarity})

with open(str(topic+'.csv'), 'w') as f:
  fieldnames = ['text', 'polarity']
  writer = csv.DictWriter(f, fieldnames=fieldnames)

  writer.writeheader()
  for item in labeled:
    writer.writerow(item)
