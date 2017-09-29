'''
Reddit API Requirement
You can’t make more than 1 request every 2 seconds (or 30 a minute)
You must not lie about your user agent
'''

# PRAW requires oauth set up in praw.ini.
import praw
from settings import Settings

# Pull the login information from the settings class.
reddit = praw.Reddit(client_id=Settings.client_id,
                     client_secret=Settings.client_secret,
                     password=Settings.password,
                     user_agent=Settings.user_agent,
                     username=Settings.username)

# Collect subreddit
subreddit = reddit.subreddit(Settings.subreddit_name)

if __name__ == '__main__':
    for submission in subreddit.hot(limit=5):
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("Score: ", submission.score)
        print("---------------------------------\n")
