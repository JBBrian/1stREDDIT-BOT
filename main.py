import praw
import os
import random
import time

# Creating reddit instance using praw documentation
reddit = praw.Reddit(client_id=os.environ.get('CLIENT_ID'),
                     client_secret=os.environ.get('CLIENT_SECRET'),
                     user_agent='<console:LOKER-BOT:v1.0',
                     username='Leto-Joker-Bot',
                     password=os.environ.get('REDDIT_PASS'))

subreddit = reddit.subreddit('h3h3productions')

# Extracting and picking a random quote from quote.txt
with open('quotes.txt', 'r') as data:
    lines = data.readlines()

# Check first 40 posts sorting by hot
for post in subreddit.hot(limit=40):
    for comment in post.comments:
        # Generate a random reply for every comment
        reply_comment = random.choice(lines)
        # Finding all comment bodies and converting to lowercase
        if hasattr(comment, 'body'):
            comment_lower = comment.body.lower()
            # Finding target word in comment (joke, joker, jokes, etc) using ' joke'
            if ' joke' in comment_lower:
                print('------------- COMMENT FOUND ------------')
                print(comment.body)
                print('----------- BOT REPLY BELOW -----------')
                comment.reply(reply_comment)
                print(reply_comment)
                # Sleep bot for 11 minutes before commenting again to prevent spamming
                time.sleep(660)