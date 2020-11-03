import praw
from bs4 import BeautifulSoup


reddit = praw.Reddit(client_id='Y_4hNDDcE9PmaA',
                     client_secret='N_rZa6RiMhZNq9KqrRNuKsQo_aOdAA',
                     user_agent='<console:crime_bot:0.0.1 (by u/Sure-Ad7152)>',
                     username="Sure-Ad7152"
                     )

"Retrieving instances from reddit with key word"
subreddit = reddit.subreddit("TrueCrime")

for post in subreddit.hot(limit=10):
    print('-------------------')
    print(post.title)


def __init__(self):
    self.request = Request()


soup = BeautifulSoup(self.request.get, 'html.parser')


class GetLink:
    for post in soup.findAll('div',
                             """class_="y8HYJ-y_lTUHkQIc1mdCq _
                             2INHSNB8V5eaWp4P0rY_mE"):"""
        links=post.find('a')
        baseURL='https://www.reddit.com/r/TrueCrime/'
        NewLinks=baseURL + links["href"]
        print(NewLinks)
