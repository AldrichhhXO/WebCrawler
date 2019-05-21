# Python Based web crawler

## CS156 

This is the implementation of a web crawler that will go through a website and take all of the information related to a particular stock.


## Key Functionalities

Will be able to crawl through an entire website and be able to 'scrape' any information that is necessary/related to a stock that we are watching.

Will incorporate an agent to be able to predict the future of the stocks that we watch based on previous statistics.



## Installation

Python 3 is required to be able to fully run this application.
Pip3 will also be needed as a tool to install various packages such as:
	1. BeautifulSoup (Parsing tool for scraping websites)
	2. Matplotlib (For plotting data from web scraping data, May be used for testing purposes.)
	3. PyMySQL For storing data into a database for easier reading of data


You will also need to download a MySQL Server to be able to run the program completely, since we use a database instead of nodes.

When downloading the server you can either make the same 'root' and 'password', or you can change it, just make sure you replace
all of the connection calls with your login information otherwise the code will not work.

Link to the MySQL server: https://dev.mysql.com/downloads/mysql/


### Installing the packages
	
	In the Requirements.txt we have all of the main modules required for our project. To install

		1. pip3 install -r requirements.txt

### Database Schema

This MySQL database will consist of two tables:

	1. StockData: Which will record the name of the stock and other information scraped from the web
	2. Queue: Which will keep track of all of the URLs and whether or not they have been scraped or not.
	3. WCData: Which will only keep track of the stock's current price


### Representation (Rule-Based)

	We will be using PyKnow, which is a python module that allows us to be able to create rules and facts and have them stored into a class (Knowledge base)

### Agent

	The Agent be initialized with certain variables:

		1. Crawler: Web crawler to serve as the main sensor for the Agent.
		2. Model: Which will contain the main stocks to search.

### Stock Prediction Algorithm

Although our stock prediction algorithm is still to be determined; possible key factors may include

	1. Looking for the lines of support and / or resistance.
	2. Dividends and stock splits
	3. Observing historic trading volumes

### Stocks

	1. Netflix



### Key Websites / Links on Stocks

	1. https://www.moneyunder30.com/how-to-read-a-stock-chart






