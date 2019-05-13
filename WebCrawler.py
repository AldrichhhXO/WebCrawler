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
		self.crawl("WebCrawler", WebCrawler.base_url)
		self.print_links()

	# Sets up the web crawler.
	@staticmethod
	def setup():
		print("Setting up.")


		#  Creates the database for the webcrawler
		create_database();

		# create_project_dir(WebCrawler.project_name)
		# create_data_files(WebCrawler.project_name, WebCrawler.base_url)
		# WebCrawler.queue = convert_to_set(WebCrawler.queue_file)
		# WebCrawler.crawled = convert_to_set(WebCrawler.crawled_file)


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
	def crawl(spider, page_url):
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
			
	
	@staticmethod
	def crawl_page(spider_name, page_url):
		if page_url not in WebCrawler.crawled:
			print(spider_name + ' now crawling ' + page_url)
			print('Queue: ' + str(len(WebCrawler.queue)) + ' | Crawled: ' + str(len(WebCrawler.crawled)))
			WebCrawler.add_links_to_queue(WebCrawler.gather_links(page_url))
			WebCrawler.queue.remove(page_url)
			WebCrawler.crawled.add(page_url)
			WebCrawler.update_files()


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


	@staticmethod
	def gett_links():
		
		con = pymysql.connect('localhost', 'root', 'ASZNkevin1', 'WebCrawler')
		with con:
			cur = con.cursor()
			sqlstatement = 'SELECT Url FROM Queue;'
			cur.execute(sqlstatement)
			ret = cur.fetchall()
			return ret



		
		