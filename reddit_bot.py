import praw


"Requirement 1 - Calling an API and getting data from a website"
reddit = praw.Reddit(client_id='VRDpHKf3yx2UDw',
                     client_secret='jXA-c7OqNOH3xPKu0crJzzaNxymldQ',
                     user_agent='<console:crime_bot:0.0.1 (u/bot_user2886)>',
                     username="bot_user2886"
                     )

"Requirement 2 - Calling 3/3 functions for data retrieval"

"Retrieving top 10 instances in the hot list on a subreddit"


def TrueCrime():
    subreddit = reddit.subreddit("TrueCrime")

    for post in subreddit.hot(limit=10):
        "Requirement 3 - Analyze text and display information about it"
        mes = len(post.title.split(" "))
        print('-------------------')
        print(post.title)
        print(post.url)
        print("The number of words in string are : " + str(mes))


TrueCrime()


def SerialKillers():

    subreddit = reddit.subreddit("serialkillers")

    for post in subreddit.hot(limit=10):
        print('-------------------')
        print(post.title)
        print(post.url)


SerialKillers()


def TCDiscussion():
    subreddit = reddit.subreddit("TrueCrimeDiscussion")

    for post in subreddit.hot(limit=10):
        print('-------------------')
        print(post.title)
        print(post.url)


TCDiscussion()
