import praw


"Requirement 1 - Calling an API and getting data from a website"
reddit = praw.Reddit(client_id='VRDpHKf3yx2UDw',
                     client_secret='jXA-c7OqNOH3xPKu0crJzzaNxymldQ',
                     user_agent='<console:crime_bot:0.0.1 (u/bot_user2886)>',
                     username="bot_user2886"
                     )


you = reddit.redditor('bot_user2886')
subreddit = reddit.subreddit('TrueCrime')

keywords = ['murder', 'serial', 'update']
ignore_users = ['baduser1', 'baduser2', 'baduser3']  # case SENSITIVE

already_alerted_submissions = []

comment_stream = subreddit.stream.comments()


def main():
    try:
        for comment in comment_stream:

            if comment.submission.id in already_alerted_submissions:
                continue

            if comment.author:  # if comment author hasn't deleted
                if comment.author.name in ignore_users:
                    continue

            for kw in keywords:
                if kw.lower() in comment.body.lower():  # case insensitive check

                    msg = '[Keyword {0} detected](http://www.reddit.com{1})'.format(kw,
                                                                                    comment.permalink())
                    you.message(subject='keyword detected', message=msg)  # send the PM
                    print(msg)

                    already_alerted_submissions.append(comment.submission.id)

    except Exception as e:
        print('There was an error: ' + str(e))
        sleep(60)  # wait for 60 seconds before restarting
        main()


if __name__ == '__main__':
    main()
