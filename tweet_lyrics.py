import tweepy
import lyricspicker

consumer_key = "ENTER KEY"
consumer_secret = "ENTER KEY"
access_token = "ENTER KEY"
access_token_secret = "ENTER KEY"
bearer_token = "ENTER KEY"

# Create a Client instance and use it to post a tweet
client = tweepy.Client(
    bearer_token="ENTER KEY",
    access_token=access_token,
    access_token_secret=access_token_secret,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret
)

line = lyricspicker.get_line()

client.create_tweet(text=line)
