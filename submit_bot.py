import praw


reddit = praw.Reddit(client_id='VRDpHKf3yx2UDw',
                     client_secret='jXA-c7OqNOH3xPKu0crJzzaNxyml',
                     user_agent='<console:crime_bot:0.0.1 (u/bot_user2886)>',
                     username="bot_user2886",
                     password="grad2009"
                     )


"Code to post from command line to subreddit"
subreddits = ['TrueCrime']
pos = 0

title = "Recent True Crime News"
url = "https://truecrimedaily.com/"


"Submit post to the correct subreddit"
subreddit = reddit.subreddit(subreddits[pos])
subreddit.submit(title, url=url)
