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

#######################################################################################
# Connection to the  database, Remember to change values below to match your instance #
#######################################################################################
con = pymysql.connect('localhost', 'root', 'ASZNkevin1')

# This wil create the database instance in the MySQL server.
def create_database():
	print("### Creating Database as State Space ###" + "\n")
	con = pymysql.connect('localhost', 'root', 'ASZNkevin1')
	with con:
		cur = con.cursor()


		cur.execute("DROP DATABASE IF EXISTS WebCrawler")

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
		


		'''
			#########################################
						Table Declaration
			urlID: The link
			url: The URL
			level: level of crawling.
			link_number: the order of crawled links in the level
			Crawled: If the link has been crawled or not.

			#########################################

		'''

		cur.execute("CREATE TABLE IF NOT EXISTS Queue \
			(UrlID INT AUTO_INCREMENT, \
			Url CHAR(200) NOT NULL, \
			Level INT NOT NULL, \
			Link_Number INT NOT NULL, \
			Crawled VARCHAR(5) NOT NULL DEFAULT 'FALSE', \
			PRIMARY KEY(UrlID));")

		#  Todo: Figure out what to store in this table. ############
		"""
			StockData table:
				StockName: Name of the stock that we scrape.
				52Wk Low: The low for the 52 week range
				52Wk High: The high for the 52 week range
				P/E
				EPS
		"""


		cur.execute("CREATE TABLE IF NOT EXISTS StockData \
			(StockID INT NOT NULL AUTO_INCREMENT, \
			StockName VARCHAR(20) NOT NULL UNIQUE, \
			52_Wk_Low FLOAT(30) NOT NULL, \
			52_Wk_High FLOAT(30) NOT NULL, \
			PriceEarnings FLOAT(30) NOT NULL, \
			EPS FLOAT(30) NOT NULL, \
			1DayPrediction FLOAT(30) NOT NULL, \
			7DayPrediction FLOAT(30) NOT NULL, \
			30DayPrediction FLOAT(30) NOT NULL, \
			PRIMARY KEY(StockID));")




	con.close()

# Inserts the link into the database, As well as the current level of the link in regards of crawling the links.
def insert_link_to_db(link, level):
	con = pymysql.connect('localhost', 'root', 'ASZNkevin1', 'WebCrawler')
	try:	
		with con:
			cur = con.cursor()

			# Find all rows that match the level that you are crawling
			rows = cur.execute("SELECT * FROM Queue WHERE level = %d", level)

			# If no rows found, first entry of the level, thus setting the value to 1.
			if (rows == 0):
				cursor.execute("INSERT INTO Queue (Url, level, link_number) VALUES (%s, %d, %d)", (link, level, 1))
			else:
				# If rows found, link_number will be set to the next number to the size of amount of current rows.
				cur.execute("INSERT INTO Queue (Url, level, link_number) VALUES (%s, %d, %d)", (link, level, (rows + 1)))
			con.commit()
	finally:
		cur.close()

'''

	This will be responsible for storing the stockdata into the database, where the Agent can reference it later.


	Note: Done, just need to test

'''
def insert_stockdata_db(stockname, low, high, PE, EPS):

	con = pymysql.connect('localhost', 'root', 'ASZNkevin1', 'WebCrawler')
	with con.cursor() as cursor:

		insert_sql = "INSERT INTO StockData(StockName, 52_Wk_Low, 52_Wk_High, PriceEarnings, EPS) \
		VALUES(%s, %s, %s, %s);"

		cursor.execute(insert_sql, (stockname, low, high, PE, EPS))

	con.close()


'''

	Possible actions caller method, might be stored into the database
	###### Check this later ############

'''
def retrieve_actions():
	return














