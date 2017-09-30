'''
Reddit API Requirement
You can’t make more than 1 request every 2 seconds (or 30 a minute)
You must not lie about your user agent
'''

# set up attributes
import praw

#import for command line arguments
import sys
import urllib.request, json

#import settings class
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
    for item in sys.argv:
        if item == '-o':
            #this bypasses praw to dump raw json into a file
            address = 'https://www.reddit.com/r/'+Settings.subreddit_name+'/hot/.json'
            # collect data from url
            with urllib.request.urlopen(address) as url:
                data = json.loads(url.read().decode())

            # Write json to file. Useful for inspecting.
            with open('subreddit.txt', 'w') as outfile:
                json.dump(data, outfile)
        else:
            #Print the top 5 hot posts
            for submission in subreddit.hot(limit=5):
                print("Title: ", submission.title)
                print("Text: ", submission.selftext)
                print("Score: ", submission.score)
                print("---------------------------------\n")
