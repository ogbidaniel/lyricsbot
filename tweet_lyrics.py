import tweepy
import lyricspicker

consumer_key = "UD5mN3IfRWTv9hPSwkoJsZT99"
consumer_secret = "A1hc72jVdLQUQFYi5sh8DJyV2n2IdfyXgWx2LZO4RoXFrmqTTk"
access_token = "1330582472418070530-bMuvf6MIIgibwtRDahjnhMwctmisv8"
access_token_secret = "rBTuD4YjljWGT7E601rbeQRDkyYt5Y6Lf5kwreunGHndp"
bearer_token = "AAAAAAAAAAAAAAAAAAAAACVWnwEAAAAAhVbY%2F%2B%2FsjR%2BlbD4SKJxpm50cazA%3D3fvJIX7xOwVktRyw3fnKWldLDPJJ9D7mJ0RnPdWyEoy3zFYyni"

# Create a Client instance and use it to post a tweet
client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAACVWnwEAAAAAhVbY%2F%2B%2FsjR%2BlbD4SKJxpm50cazA%3D3fvJIX7xOwVktRyw3fnKWldLDPJJ9D7mJ0RnPdWyEoy3zFYyni",
    access_token=access_token,
    access_token_secret=access_token_secret,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret
)

line = lyricspicker.get_line()

client.create_tweet(text=line)
