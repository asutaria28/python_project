import praw


reddit = praw.Reddit(client_id='VRDpHKf3yx2UDw',
                     client_secret='jXA-c7OqNOH3xPKu0crJzzaNxymldQ',
                     user_agent='<console:crime_bot:0.0.1 (u/bot_user2886)>',
                     username="bot_user2886"
                     )

"Retrieving top 10 instances in the hot list on a subreddit"
subreddit = reddit.subreddit("TrueCrime")

for post in subreddit.hot(limit=10):
    print('-------------------')
    print(post.title)
