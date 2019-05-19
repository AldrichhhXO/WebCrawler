'''

	#################################################################
	This is the environment class; which will model the environment portion
	of the agent.


	This file will consist of the following:
		1. URL: Link to the webpage that will be crawled.
		2. Methods for the agent to be able to see information in the
		website.

	
	CS 156 Final Project
	Group 8
	May 13, 2019
	#################################################################
'''

from WebCrawler import *

'''
	#################################################################
	Environment class

	Variables:
		1. agents: Web Crawling agents currently attached to the environment
			(1 for now)
		2. Page_urls: Page_urls that will be queued and crawled (Might take this out)

	#################################################################

'''

class Environment:	
	
	def __init__(self, page_url, DOMAIN_NAME, agent):
		self.agents = agent
		self.page_url = page_url


	# Percept function to attain all the data we need.
	def percept(self, agent):
		

		






