'''
	This is the extra credit assignment for the project.

	Search Algorithm: Iterative deepening.

	To-do: Construct a driver program that is capable of searching a specific state-space


	Aldrich Reboja
	CS156
	May 15, 2019


''' 
import time
import pymysql
import requests
from WebCrawler import *
from Memory import *


'''
	Iterative deepening method:

	1. Top depth (Root) will start at zero


	Params:
		1. 'Problem' : Which will describe the problem to be solved.
		in this example, the problem will be finding links to crawl.



		****    Done    ****
'''
def iterative_deepening_search(problem, crawler, limit):
	print('######## Testing Iterative Deepening algorithm ######' + '\n')

	cutoff = 'Link not found'

	# from the root to an infinite number
	for depth  in range(0, 100):
		result = depth_limited_search(problem, crawler, depth)
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
			3.	depth: The depth of where to search; searches all links in that depth (Left to right)

	#######################################################
'''
def depth_limited_search(problem, crawler, depth):
	# Establish connection to the database
	print('DLS on depth: ' + str(depth))

	con = pymysql.connect('localhost', 'root', 'ASZNkevin1', 'WebCrawler')
	try:
		with con:
			# Select all the links that match the depth and link number being called.
			cur = con.cursor()

			links = "SELECT * FROM Queue WHERE depth = %s;"
			linkRes = cur.execute(links, depth)
			if linkRes == 0:
				return

			ret = cur.fetchall()
			for entry in ret:
				# print(entry[1])
				for stock in problem:
					if stock in entry[1]:
						print('Found the link: ' + entry[1] + '\n')
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

##################################################
# Can Change this url to change testing methods.
base_url = 'https://www.investopedia.com'
domain_name ='investopedia.com'





# Set up the state space to undergo the search
crawler = WebCrawler(project_name, base_url, domain_name)
crawler.crawl(project_name, base_url, 0)
# crawler.setup()

# Call to the iterative deepening algorithm, searching for certain links
start_time = time.time()

# The problem to solve, finding the link for the Apple stock information. Ex: 'Domain_name.com/AAPL'
goal = {'tsla'}
search_result = iterative_deepening_search(goal, crawler, 2)
elapsed = time.time() - start_time
print("Time to search: " + str(elapsed))


goal = {'aapl'}
start_time = time.time()
search_result = iterative_deepening_search(goal, crawler, 2)
elapsed = time.time() - start_time
print("Time to search: " + str(elapsed))


goal = {'xqdsjn'}
start_time = time.time()
search_result = iterative_deepening_search(goal, crawler, 2)
elapsed = time.time() - start_time
print("Time to search: " + str(elapsed))















