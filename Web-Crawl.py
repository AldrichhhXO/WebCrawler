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
	 #print(plain_text)

	 html_doc ="""
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset = "UTF-8">
	<meta name = "viewport" content="width=device=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>My Webpage</title>
</head>
<body>
	<div id="section-1">
	<h3 data-hello="hi">hello</h3>
	<img src ="https://source.unsplash.com/200x200/?
	nature,water" />
	<p>Lorem ipsum dolor, sit amet consectetur
	adepisicing elit. Fuga obcaecati quam sed
	blanditiis! Quaerat tempore suscipit,
		neque temporibus commodi nostrum qui magnam, totam
	</p>
</body>
</html>
"""


	# Initialization of BeautifulSoup4
	# soup = BeautifulSoup(plain_text, 'html.parser')
	soup = BeautifulSoup(html_doc, 'html.parser')

	# Finds the first instance of the <a> (Hyperlink) element

	# Function call to the Investopedia crawl
	investopedia_Crawl(soup)



yung_spider()


