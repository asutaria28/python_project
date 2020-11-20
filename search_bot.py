import praw
# from time import sleep

"Requirement 1 - Calling an API and getting data from a website"
reddit = praw.Reddit(client_id='VRDpHKf3yx2UDw',
                     client_secret='jXA-c7OqNOH3xPKu0crJzzaNxymldQ',
                     user_agent='<console:crime_bot:0.0.1 (u/bot_user2886)>',
                     username="bot_user2886"
                     )


you = reddit.redditor('bot_user2886')
subreddit = reddit.subreddit("TrueCrime")

"Requirement 3- Create a list and use an item to retrieve results"
keywords = ['Case']
ignore_users = ['baduser1', 'baduser2', 'baduser3']

already_alerted_submissions = []

post_stream = subreddit.stream.submissions()

"Requirement 2 - Calling 3rd function"


def main():
    titles = []
    for post in post_stream:
        titles.append(post.title)
    print(titles)
    # try:
    #    for post in post_stream:

    #        if post.title in already_alerted_submissions:
    #         continue

    #        if post.author:
    #          if post.author.name in ignore_users:
    #                continue

    # for kw in keywords:
    #    if kw.lower() in post.title.lower():
    #        msg = '[Keyword {0} detected](http://www.reddit.com{1})'.format(kw,
    #                                                                        post.permalink())
    #        you.message(subject='keyword detected', message=msg)
    #        print(msg)

    #            already_alerted_submissions.append(post.title)

#    except Exception:
#        raise
#        print('There was an error')
    #    sleep(60)
    #    main()


#    if __name__ == '__main__':
main()
