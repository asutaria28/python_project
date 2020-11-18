import praw
from time import sleep

"Requirement 1 - Calling an API and getting data from a website"
reddit = praw.Reddit(client_id='VRDpHKf3yx2UDw',
                     client_secret='jXA-c7OqNOH3xPKu0crJzzaNxymldQ',
                     user_agent='<console:crime_bot:0.0.1 (u/bot_user2886)>',
                     username="bot_user2886"
                     )


you = reddit.redditor('bot_user2886')
subreddit = reddit.subreddit('TrueCrime')

"Requirement 3 - Create a list and use an item to retrieve results"
keywords = ['murder', 'serial', 'update']
ignore_users = ['baduser1', 'baduser2', 'baduser3']

already_alerted_submissions = []

comment_stream = subreddit.stream.comments()

"Requirement 2 - Calling 3rd function"


def main():
    try:
        for comment in comment_stream:

            if comment.submission.id in already_alerted_submissions:
                continue

            if comment.author:
                if comment.author.name in ignore_users:
                    continue

            for kw in keywords:
                if kw.lower() in comment.body.lower():
                    msg = '[Keyword {0} detected](http://www.reddit.com{1})'.format(kw,
                                                                                    comment.permalink())
                    you.message(subject='keyword detected', message=msg)
                    print(msg)

                    already_alerted_submissions.append(comment.submission.id)

    except Exception as e:
        raise
        print('There was an error: ' + str(e))
        sleep(60)
        main()

    main()
