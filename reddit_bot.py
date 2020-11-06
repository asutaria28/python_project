import praw

decision = input("Do you want to post or view a subreddit? Enter post/view:")

"Requirement 1 - Calling an API and getting data from a website"
reddit = praw.Reddit(client_id='VRDpHKf3yx2UDw',
                     client_secret='jXA-c7OqNOH3xPKu0crJzzaNxymldQ',
                     user_agent='<console:crime_bot:0.0.1 (u/bot_user2886)>',
                     username="bot_user2886"
                     )

"Requirement 2 - Populating a class"


class TrueCrime:

    "Retrieving top 10 instances in the hot list on a subreddit"
    subreddit = reddit.subreddit("TrueCrime")

    for post in subreddit.hot(limit=10):
        print('-------------------')
        print(post.title)
        print(post.url)


class SerialKillers:

    subreddit = reddit.subreddit("serialkillers")

    for post in subreddit.hot(limit=10):
        print('-------------------')
        print(post.title)
        print(post.url)
