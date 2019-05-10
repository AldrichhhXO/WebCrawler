import os

# Importing the MySQL module
import pymysql

"""
	This file will be responsible for keeping track of the crawled links within the website.
	Will have two different types of memory; depending on how you want to keep track of the  info
		1. Text file; which will be updated through every iteration of the crawl.
		2. Database: Which will be used the same way but in a more organized manner.


	ToDo (If time): Convert the sql functons below into a sql file and read from there.

"""

# Connection to the  database
con = pymysql.connect('localhost', 'root', 'ASZNkevin1')

# This wil create the database instance in the MySQL server.
def create_database():
	print("### Creating database ###" + "\n")
	con = pymysql.connect('localhost', 'root', 'ASZNkevin1')
	with con:
		cur = con.cursor()

		cur.execute("CREATE DATABASE IF NOT EXISTS WebCrawler;")
		print("WebCrawler Database initialized \n")

		cur.close()
	initialize_tables()
		

# Initializing the tables for the webcrawler
def initialize_tables():
	print("### Initializing Tables ###" + "\n")
	con = pymysql.connect('localhost', 'root', 'ASZNkevin1', 'WebCrawler')
	with con:
		cur = con.cursor()
		
		#	#############	Added to Keep the tables each time it's run.	#############	#
		cur.execute("DROP TABLE IF EXISTS Queue")

		cur.execute("CREATE TABLE IF NOT EXISTS Queue \
			(UrlID INT AUTO_INCREMENT, \
			Url CHAR(200) NOT NULL, \
			Crawled VARCHAR(5) NOT NULL DEFAULT 'FALSE', \
			PRIMARY KEY(UrlID));")

		#  Todo: Figure out what to store in this table. ############
		"""
			StockData table:
				StockName: Name of the stock that we scrape.
				urlID: Reference as to where the url came from. (may not need)

			cur.execute("CREATE TABLE IF NOT EXISTS StockData \
			(StockName VARCHAR(20), \
			urlID INT NOT NULL \
			FOREIGN KEY (urlID) REFERENCES Queue(UrlID));")

		"""
	con.close()





# Inserts the link into the database.
def insert_link_to_db(link):
	con = pymysql.connect('localhost', 'root', 'ASZNkevin1', 'WebCrawler')
	try:	
		with con:
			cur = con.cursor()
			cur.execute("INSERT INTO Queue (Url) VALUES (%s)", link)
			con.commit()
	finally:
		cur.close()



# Each website you crawl is a separate project (folder)
def create_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating project ' + directory)
		os.makedirs(directory)

# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')

# Create a new file
def write_file(path, link):
	f = open(path, 'w')
	f.write(link)
	f.close()

# Adds a new link to crawl.
def addData(path, link):

	# 'a' is Append mode
	with open(path, 'a') as file:
		file.write(link + '\n')

# Delete The contents of a file
def delete_content(path):
	with open(path, 'w'):
		pass	# do nothing

# Using a set to keep the crawled/queued files unique, skipping the crawls.

# Read a file and convert each line to set items.
def convert_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results

# Convert a set to a file
"""
	first deletes the old data
	Then inserts updated data.
"""
def convert_to_file(links, file):
	delete_content(file)
	for link in sorted(links):
		addData(file, link)

# create_data_files('stocks', 'https://www.investopedia.com')

# create_project_dir('stocks')