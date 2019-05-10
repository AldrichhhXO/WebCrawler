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
class YungSpider:


	# Name of the folder containing the files
	project_name = ''
	base_url = ''
	domain_name =''

	links = set()



	# Called when spider is created.
	def __init__(self, project_name, base_url, domain_name):

		# Initialization of the Yung Spider.
		print("Initializing")
		YungSpider.project_name = project_name
		YungSpider.base_url = base_url
		YungSpider.domain_name = domain_name

		# Seta up the web crawler for the project.
		self.setup()
		self.crawl("YungSpider", YungSpider.base_url)

		# self.crawl_page('yeet', YungSpider.base_url)

	# Sets up the web crawler.
	@staticmethod
	def setup():
		print("Setting up.")


		#  Creates the database for the webcrawler
		create_database();

		# create_project_dir(YungSpider.project_name)
		# create_data_files(YungSpider.project_name, YungSpider.base_url)
		# YungSpider.queue = convert_to_set(YungSpider.queue_file)
		# YungSpider.crawled = convert_to_set(YungSpider.crawled_file)


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
					links = YungSpider.gather_links(page_url)
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
		if page_url not in YungSpider.crawled:
			print(spider_name + ' now crawling ' + page_url)
			print('Queue: ' + str(len(YungSpider.queue)) + ' | Crawled: ' + str(len(YungSpider.crawled)))
			YungSpider.add_links_to_queue(YungSpider.gather_links(page_url))
			YungSpider.queue.remove(page_url)
			YungSpider.crawled.add(page_url)
			YungSpider.update_files()


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

			# print(data.get('href'))
			result.add(data.get('href'))

		print("Links found : " + str(len(result)))
		return result



		
		