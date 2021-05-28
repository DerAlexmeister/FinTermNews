#!/usr/bin/python3

import os
import re
import shutil
import feedparser

from colorama import init as color_init
from termcolor import colored

news_feeds = {
	"Apple": "https://www.finanzen.net/rss/apple-rss-feed"
}

#shutil.get_terminal_size((1920,1080))

terminal_width = tuple(os.get_terminal_size())

def pretty_print(data):
	for entry in data.entries:
		print(colored(entry.title, 'cyan', attrs=['bold']))
		print(colored("   [>>] ", 'green'), entry.published)
		print(colored("   [>>] ", 'green'), entry.link)
		print()

def fetch_rss_feed():
	for feed_title, feed in news_feeds.items():
		print("---- {} ".format(colored(feed_title, 'blue')) + "-"*(terminal_width[0]-(len(feed_title)+6)))
		NewsFeed = feedparser.parse(feed)
		pretty_print(NewsFeed)
	print("-"*terminal_width[0])

color_init()
fetch_rss_feed()
