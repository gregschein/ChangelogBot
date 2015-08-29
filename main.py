import praw
import time

r = praw.Reddit('Dota 2 changelog bot')
r.login()

while True:
	subreddit = r.get_subreddit('dota2')
	for submission in 