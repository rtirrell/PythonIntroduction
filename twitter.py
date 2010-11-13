from smalltweetlib import get_tweets

tweets = get_tweets('cnn')

for tweet in tweets:
  print tweet['text']


