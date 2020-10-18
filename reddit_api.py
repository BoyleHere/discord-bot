import praw
from config import *
import random

reddit = praw.Reddit(client_id = REDDIT_APP_ID, 
					 client_secret = REDDIT_SECRET,
					 username = USERNAME,
					 password = PASSWORD,
					 user_agent = USER_AGENT)

def meme(subreddit):
	chosen_subreddit = ''
	if subreddit:
		chosen_subreddit = subreddit
	else:
		chosen_subreddit = 'dankmemes'

	submissions = reddit.subreddit(chosen_subreddit).hot()
	post = random.randint(1, 30)
	for i in range (0, post):
		submission = next(x for x in submissions if not x.stickied)
	return submission