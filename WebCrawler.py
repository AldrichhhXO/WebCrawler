from Memory import *
from bs4 import BeautifulSoup
import requests

"""
	Spider Implementation.

	Notes: 

	Originally utilizing text files to store link data; will be implementing a database to be able
	to insert all  of the links into a database and be able to read as well.


	When instantiated; The webcrawler will:
		1. Setup: Initialize the  database and tables.
		2. Crawl the page.

"""
class WebCrawler:


	# Name of the folder containing the files
	project_name = ''
	base_url = ''
	domain_name =''

	# SET OF STOCKS TO LOOK FOR INSIDE THE WEBSITE
	stocks  = {'AAPL',  'TSLA', 'NFLX', 'AMZN'}
	links = set()



	# Called when spider is created.
	def __init__(self, project_name, base_url, domain_name):

		# Initialization of the Yung Spider.
		print("Initializing")
		WebCrawler.project_name = project_name
		WebCrawler.base_url = base_url
		WebCrawler.domain_name = domain_name

		# Seta up the web crawler for the project.

		# Commented for testing purposes
		self.setup()
		# self.crawl("WebCrawler", WebCrawler.base_url)
		self.print_links()

	# Sets up the web crawler.
	@staticmethod
	def setup():
		print("Setting up.")


		#  Creates the database for the webcrawler
		create_database();

	"""
		Database version of the crawl page method.
		Overall Functionality:
			1. Checks if the page is already crawled.
				- If so then done. lol
			2. If not then add it into the database.
			3. Update the page URL in db to say its been crawled.
			4. Recursively call add links to db.

	"""
	@staticmethod
	def crawl(spider, page_url, level):
		print('################# Crawling '  + page_url + ' ####################')
		con = pymysql.connect('localhost', 'root', 'ASZNkevin1', 'WebCrawler')
		try:
			with con:
				cur = con.cursor()	

				# Insert if this is the very first  website  URL.
				countsql = "SELECT * FROM Queue;"

				insertsql =  "INSERT INTO QUEUE (Url) VALUES(%s);"

				# Checks the amount links currently in the table.
				numLinks = cur.execute(countsql)
				print('!!!!!!!!!!!!    ' +  str(numLinks)  +  '      !!!!!!!!!!!')

				# if this is the very first link, insert and then crawl it.
				if numLinks == 0:
					cur.execute(insertsql, page_url)
					con.commit()


			# ################	If the current link has not been crawled, Crawl the link and update the value ########### #
				resultNumber = cur.execute("SELECT * FROM Queue WHERE Url = %s AND Crawled = 'False';", page_url)
				if resultNumber == 0: 
					print('####### Link  Crawled.....')
					return
				else:
					print(spider  +  ' now crawling '  +  page_url)
					print('Queue: ')

					# Gathers all of the links intoa set.
					links = WebCrawler.gather_links(page_url)
					print('################## Amount of links crawled:' + str(len(links)) +  ' #################')
					for link in links:
						insert_link_to_db(link)
						print(link + '\n')
						# cur.execute("INSERT INTO Queue (Url) VALUES(%s)", link)


					updateSQL = "UPDATE Queue SET  Crawled = 'TRUE' WHERE Url = %s"
					# Updates the crawled variable to be set to TRUE.
					cur.execute(updateSQL, page_url)
					con.commit()


		finally:
			con.close()
			

		"""
		Connects to a site
		Extracts the HTML in byte
		Converts the byte into readables.
		Gets all of the links.

	"""
	@staticmethod
	def gather_links(page_url):

		result = set()

		# Gets the request and then converts into the HTML text.
		source_code = requests.get(page_url)
		plain_text = source_code.text

		# HTML parser for the website.
		soup = BeautifulSoup(plain_text, 'html.parser')
		for data in soup.find_all('a'):
			# print(data)

			# Check if the link is in the same domain otherwise don't use.
			parsedLink =  data.get('href')
			if WebCrawler.domain_name in parsedLink:
				result.add(data.get('href'))

		print("Links found : " + str(len(result)))
		return result


	'''
		######################################################################
		This method is a getter method for the links.

		######################################################################
	'''
	@staticmethod
	def print_links():
		
		con = pymysql.connect('localhost', 'root', 'ASZNkevin1', 'WebCrawler')
		with con:
			cur = con.cursor()
			sqlstatement = 'SELECT * FROM Queue;'
			cur.execute(sqlstatement)
			ret = cur.fetchall()
			for r in ret:
				print(r)


	'''
		######################################################################

		This method is a getter method for the links; will return a variable of all the links
		
		######################################################################


	'''
	@staticmethod
	def get_links():
		
		con = pymysql.connect('localhost', 'root', 'ASZNkevin1', 'WebCrawler')
		with con:
			cur = con.cursor()
			sqlstatement = 'SELECT Url FROM Queue;'
			cur.execute(sqlstatement)
			ret = cur.fetchall()
			return ret


	'''

		This is the method that will be responsible for collecting all the data on the top portion of the
		page.

	'''
	@staticmethod
	def retrieve_stock_data(link):

		# Gets the request and then converts into the HTML text.
		source_code = requests.get(link)
		plain_text = source_code.text

		# print(plain_text)


		# HTML parser for the website.
		soup = BeautifulSoup(plain_text, 'html.parser')
		result = soup.find_all('tr')


		for r in result:
			print(r.td)

		#print(result)
			


		# gets the header of that corresponding row.
		# adding the 'text' call retrieves the actual text within the header tag.
		# print(result.th.text)




		


		
		