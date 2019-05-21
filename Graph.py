import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from Memory import *


'''
	This is the graph class, that will be responsible for graphing the stock data.

	holds the stock that will be graphed.

'''
class Graph():

	def __init__(self, stockSet):
		self.name = stockSet
	
	'''

		Method that will be called to graph the stock past to current data.

	'''
	@staticmethod
	def graph_stocks(stockName):
		style.use('ggplot')

		# Hard coded dates to cover a wide range of data
		start = dt.datetime(2000,1,1)
		end = dt.datetime(2019,5,19)

		# df = web.DataReader('AAPL', 'yahoo', start, end)
		df = web.DataReader(stockName, 'yahoo', start, end)
		print(df)
		df['High'].plot()
		plt.show()


	'''

	Function to store the stock data into the db.

	'''
	@staticmethod
	def data_to_db(stockName):
		style.use('ggplot')
		print('yeeeee')

		con = pymysql.connect('localhost', 'root', 'ASZNkevin1', 'WebCrawler')
		with con.cursor() as cur:
			df = pd.read_csv('appl.csv', parse_dates=True, index_col=0)
			for x in range(0,len(df)):

				high = df.iloc[x, 0]
				low = df.iloc[x, 1]
				open = df.iloc[x,2]
				close = df.iloc[x,3]
				vol = df.iloc[x,4]
				ac = df.iloc[x,5]


				# print(reee)


graph = Graph('AMZN')
# graph.graph_stocks(graph.name)
graph.data_to_db(graph.name)

