from Memory import *
from bs4 import BeautifulSoup
import requests

"""
	Spider Implementation.

	Notes: 

	Originally utilizing text files to store link data; will be implementing a database to be able
	to insert all  of the links into a database and be able to read as well.

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


		self.setup()
		self.crawl_page('yeet', YungSpider.base_url)

	# Sets up the web crawler.
	@staticmethod
	def setup():
		print("Setting up.")

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
	def crawl(spider, page_url):
		con = pymysql.connect('localhost', 'root', 'ASZNkevin1', 'WebCrawler')
		with con:
			cur = con.cursor()

			# ################	If the current link has not been crawled, Crawl the link and update the value ########### #

			resultNumber = cur.execute("SELECT * FROM Queue WHERE Url = ? AND Crawled = 'False';", page_url)
			if (resultNumber ==0) return
			else {

			# Updates the crawled variable to be set to TRUE.
			cur.execute("UPDATE Queue SET Crawled = 'True' WHERE Url = '?'", page_url)
			}

	
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


		# links will be a set
	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if url in YungSpider.queue:	# if already in queued 
				continue
			if url in YungSpider.crawled:
				continue
			if YungSpider.domain_name not in url: # makes sure that it crawls within the domain.
				continue
			YungSpider.queue.add(url)

	@staticmethod
	def update_files():
		convert_to_file(YungSpider.queue, YungSpider.queue_file)
		convert_to_file(YungSpider.crawled, YungSpider.crawled_file)






		
		