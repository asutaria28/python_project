import praw
import os


"Requirement 1 - Calling an API and getting data from a website"
reddit = praw.Reddit(client_id='VRDpHKf3yx2UDw',
                     client_secret=os.environ.get('Client_Secret'),
                     user_agent='<console:crime_bot:0.0.1 (u/bot_user2886)>',
                     username="bot_user2886"
                     )

"Requirement 2 - Calling 2/3 functions for data retrieval"

"Retrieving top 10 instances in the hot list on a subreddit"


def TrueCrime():
    subreddit = reddit.subreddit("TrueCrime")

    for post in subreddit.hot(limit=10):
        print('-------------------')
        print(post.title)
        print(post.url)


TrueCrime()


def SerialKillers():

    subreddit = reddit.subreddit("serialkillers")

    for post in subreddit.hot(limit=10):
        print('-------------------')
        print(post.title)
        print(post.url)


SerialKillers()
