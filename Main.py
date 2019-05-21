from WebCrawler import *
from Agent import *
# Importing Graph plotting module
import matplotlib.pyplot as plt 



'''
	This can be changed at any time to try with different websites.
'''
PROJECT_NAME = 'WebCrawler'
BASE_URL = 'https://www.investopedia.com'
DOMAIN_NAME = 'investopedia.com'


'''
	
	Sensor

'''

# Agent = Agent(WebCrawlerAgent(BASE_URL))


# Testing that the web crawler works
# wc = WebCrawler(PROJECT_NAME, BASE_URL, DOMAIN_NAME)
# wc.setup()



# This will initialize an Agent, with a webcrawling agent program.
webCrawlingAgent = Agent(BASE_URL)

# webCrawlingAgent.crawler.crawl("YEET", BASE_URL, 0, 1)
# webCrawlingAgent.crawler.retrieve_stock_data('AMZN','https://www.investopedia.com/markets/stocks/amzn/')

'''
	Save this one for later; may need to be like this for the end code.	
'''

# Environment(BASE_URL, DOMAIN_NAME, WebCrawler(PROJECT_NAME, BASE_URL, DOMAIN_NAME))