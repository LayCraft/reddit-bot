'''
Reddit API Requirement
You can’t make more than 1 request every 2 seconds (or 30 a minute)
You must not lie about your user agent
'''

# PRAW requires oauth set up in praw.ini.
import praw

#these must be changed for the bot to work
subredditToCrawl = "bi4l"
'''
Here is a template for password entry and loggin in
reddit = praw.Reddit(client_id=clientID,
                     client_secret='xaxkj7HNh8kwg8e5t4m6KvSrbTI',
                     password='1guiwevlfo00esyy',
                     user_agent='testscript by /u/fakebot3',
                     username='fakebot3')
'''
reddit = praw.Reddit(client_id='k3fnUT5fXfuhUg',
                     client_secret='u2YzqG87PqtPQpAa5JdHuWuTrFE',
                     password='thirdr0ck',
                     user_agent='BI4L Bot 0.1 by mrtherapist',
                     username='mrtherapist')

# Collect subreddit
subreddit = reddit.subreddit(subredditToCrawl)

if __name__ == '__main__':
    # print('Hello world')
    for submission in subreddit.hot(limit=5):
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("Score: ", submission.score)
        print("---------------------------------\n")
