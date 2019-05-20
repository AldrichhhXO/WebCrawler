from WebCrawler import *
from Agent import *
# Importing Graph plotting module
import matplotlib.pyplot as plt 



'''
	This can be changed at any time to try with different websites.
'''
PROJECT_NAME = 'WebCrawler'
BASE_URL = 'https://www.yahoo.com'
DOMAIN_NAME = 'yahoo.com'


'''
	
	Sensor

'''
WebCrawler(PROJECT_NAME, BASE_URL, DOMAIN_NAME)


# This will initialize an Agent, with a webcrawling agent program.
#webCrawlingAgent = Agent(BASE_URL, None)
#webCrawlingAgent.crawler.retrieve_stock_data('https://www.investopedia.com/markets/stocks/amzn/')

'''
	Save this one for later; may need to be like this for the end code.	
'''

# Environment(BASE_URL, DOMAIN_NAME, WebCrawler(PROJECT_NAME, BASE_URL, DOMAIN_NAME))