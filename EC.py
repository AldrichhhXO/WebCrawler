'''
	This is the extra credit assignment for the project.

	Search Algorithm: Iterative deepening.

	To-do: Construct a driver program that is capable of searching a specific stat-space


	Aldrich Reboja
	CS156
	May 15, 2019


''' 
import pymysql
import itertools
import requests
from WebCrawler import *
from Memory import *


'''
	Iterative deepening method:

	1. Top level (Root) will start at zero


	Params:
		1. 'Problem' : Which will describe the problem to be solved.
		in this example, the problem will be finding links to crawl.
'''
def iterative_deepening_search(problem, crawler, limit):
	print('######## Testing Iterative Deepening algorithm ######')

	cutoff = 'Link not found'

	for depth = 0 in itertools.count():
		result = depth_limited_search(problem, crawler.stocks, depth)
		if result != cutoff:
			return result
		elif depth == limit:
			return cutoff

'''
	#######################################################
		Depth limited search, which will be used in the ID algorithm.

		Parameters:
			1.  problem: A set representing of the info to find
			2.	crawler: Webcrawler to retain conditions for the links
			3.	depth: The depth of where to search; searches all links in that level (Left to right)

	#######################################################
'''
def depth_limited_search(problem, crawler, depth):
	# Establish connection to the database
	con = pymysql.connect('localhost', 'root', 'ASZNkevin1', 'WebCrawler')
	try:
		with con:

			# Select all the links that match the level and link number being called.
			cur = con.cursor()
			links = "SELECT * FROM Queue WHERE Level = %d"
			cur.execute(links, depth)
			ret = cur.fetchall()
			for entry in ret:
				for stock in problem:
					if stock in entry:
						print('Found the link: ' + entry)
						return 'Link Found'
	finally:
		con.close()
		return 'Link not found'

'''
	#######################################################
		Web-Crawler implementation to test.
	#######################################################

'''

# Initialize the web crawler params
project_name = 'ExtraCredit'

# Can Change this url to change testing methods.
base_url = 'https://www.investopedia.com'
domain_name ='investopedia.com'


# The problem to solve, finding the link for the Apple stock information. Ex: 'Domain_name.com/AAPL'
goal = {'AAPL'}


crawler = WebCrawler()
crawler.setup()

# Call to the iterative deepening algorithm, searching for certain links
iterative_deepening_search(goal, crawler)
















