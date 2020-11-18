# python_project

Bot Project Description:
This project has three components:
- A bot that goes into two subreddits and pulls titles of the hot 10 posts for the day and the
  url below it in the console.
 - A bot that automatically uploads posts to a subreddit from the command console.
 - A bot that searches for keywords in a subreddit and pulls the results into the console.

The purpose of these bots is to be able to scrape reddit to get specific posts and information
that gets printed in the console.  The API for reddit is used in all three elements of the
reddit bot.  Three functions are used to perform needed actions in the files to search keywords
and pull the hot 10 posts on subreddits.  A list is needed to put keywords in the search_bot
element that will allow it to search for those words.  Finally, the search_bot element is
a web scrapper that searches reddit and pulls posts that mention specific keywords.

Three features included in this project:
1. Connect to an external/3rd party API and read data into your app
2. Create and call at least 3 functions, at least one of which must return a value that is used
3. Create a dictionary or list, populate it with several values, retrieve at least one value,
  and use it in your program
4. Implement a “scraper” that can be fed a type of file or URL and pull
  information off of it. For example, a web scraper that lets you provide any website URL
  and it will find certain keywords on the page

  Special instructions:
  Reddit_bot - The API is set up already with the secret key and user password located
  in a gitignore file for privacy.  For my purposes, I wanted to pull the hot 10 posts and the URL
  for two true crime subreddits.  If you wish to pull posts from a different subreddit, the subreddit
  will need to be changed on line 17 and 30 inside the parenthesis.  Please make sure the subrreddit
  name is exactly as it is on reddit.com.  Run the program in the command console.

  Submit_bot- This element will post a true crime website to the subreddit 'TrueCrime' as it is.
  If you would like to post something new to a different subreddit, the subreddit name will need
  to be replaced in the brackets on line 13 (subreddit name needs to be inserted exactly as
  it is on reddit.com). You will also need to change the title of your post on line 16,
  and  the url of what you want included in the posts on line 17. Run the program in the
  command console.

  Search bot- This element is essentially a web scraper that takes keywords from the list
  and searches a specified subreddit for posts that mention the keywords.  To searches
  keywords in a different subreddit than the true crime subreddit that is set up in the
  currently, you will need to replace the subreddit name on line 13 in the parenthesis (subreddit
    name needs to be inserted exactly as it is on reddit.com).
  You will then need to put your keywords in the list for searching in the brackets
  on line 16. Finally, run the program in the command console.
