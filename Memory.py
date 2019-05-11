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
