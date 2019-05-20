import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web



class Graph():
	
	def graph_stock(stockName):
		style.use('ggplot')

		start = dt.datetime(2000,1,1)
		end = dt.datetime(2019,5,19)

		df = web.DataReader('AAPL', 'yahoo', start, end)
		df['High'].plot()
		plt.show()

	start = dt.datetime(2000,1,1)
	end = dt.datetime(2019,5,19)


	df = web.DataReader('AAPL', 'yahoo', start, end)
	df.to_csv('appl.csv')	

	df['High'].plot()
	# df2['High'].plot()
	# df3['High'].plot()
	plt.show()

