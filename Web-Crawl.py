import requests
from bs4 import BeautifulSoup


'''
	################## TESTING FILE OF WEB CRAWLING; WILL NOT BE USING ##############

'''


"""
	This is a function that is specifically for Investopedia based websites.
	Note: Created a specific function for now in case we want to choose another website;
	This function allows parsing of the whole html page that has a specific template that should
	be the same across various stocks pages.

"""
def investopedia_Crawl(soup):

	# Retrieves all <td> elements that have the class name = 'num'
	yeet = soup.find_all('td', {'num'})

	# For loop that prints through all of the <td> elements
	for data in soup.find_all('td', {'num'}):
		print(data.string)

# The Yung Spider construction
def yung_spider():
	# url = 'https://indeks.kompas.com/news/2017-08-04/'  # Has the url change pages.
	# Investopedia  Apple Stocks url example
	url = 'https://www.investopedia.com/markets/stocks/aapl/'

	# Retrieves the data that is contained within the request call.
	source_code = requests.get(url)

	# Extracts the html code from that request
	plain_text = source_code.text

	# Initialization of BeautifulSoup4
	soup = BeautifulSoup(plain_text, 'html.parser')

	# Finds the first instance of the <a> (Hyperlink) element

	# Function call to the Investopedia crawl
	investopedia_Crawl(soup)



yung_spider()


