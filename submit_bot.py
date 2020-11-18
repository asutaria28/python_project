import praw
import os


reddit = praw.Reddit(client_id='VRDpHKf3yx2UDw',
                     client_secret=os.environ.get('Client_Secret'),
                     user_agent='<console:crime_bot:0.0.1 (u/bot_user2886)>',
                     username="bot_user2886",
                     password=os.environ.get('User_Password')
                     )


"Code to post from command line to subreddit"
subreddits = ['TrueCrime']
pos = 0

title = "Recent True Crime News"
url = "https://truecrimedaily.com/"


"Submit post to the correct subreddit"
subreddit = reddit.subreddit(subreddits[pos])
subreddit.submit(title, url=url)
