"""

	This will be the implementation of the agent class

	Based on the sample code from chapter 2. (http://aima.cs.berkeley.edu/python/agents.py);

		1. Object	# Physical object that can  exist in an environment
			- Agent  

		2. Environment # Holds objects; runs simulations


		############## Notes about agents: ############
		1. Agent = architecture + program
			Ex: If the program is going to recommend actions like
			walk; then the agent architecture better have legs.
		2. Agent Programs:
			- Agent Programs are FUNCTIONS not  CLASSES.
			- The mapping from percepts to actions.	
			- Take the current percept as input from sensors and return an action
				to the actuators
			- Just takes the current input because nothing more is available from 
				the environment.

			Note: Actuators in this project would be:
				1. Predicting algorithm
				2. Graph representation.
				3. Tables in the database; just for visual display.	

"""



''' 
 agent. (Model Based)

	variables:
		
		- stocks_percept: Will hold information on the stock information

	Self initialization:
		
'''



'''
	Agent that will exist within the website (environment), web-crawling through
	numerous amounts of data, with various amounts of actions/percepts.

	Overview:
		1.Sensors:  Web crawler scraping the data
		2. Environment: Websites; numerous links at least 100 at  a time.
		3.Actuators: Graph  representation; continue to crawl if no data


	Variables: 
		1. decision: Overall decision in regards to buying/selling stocks

'''
# from WebCrawler import *
# from Memory import *
# # from KnowledgeBase import *
# import collections


# import numpy as np
from random import choice
from pyknow import *
from array import *
from WebCrawler import *



#averagepurchase_price=50
#PRICE_high=averagepurchase_price*1.3
#PRICE_low=averagepurchase_price*0.8

#PRICE=0#[50,60,70]
#PRICE_high=1.3 * PRICE#[100,80,120]
#PRICE_low=.8 * PRICE#[50,40,30]  
ApplePurchesedPrice = 50
AmazonPurchesedPrice = 25 
NetflixPurchesedPrice = 59      
# PRICE_low=[ApplePurchesedPrice * .8, AmazonPurchesedPrice * .8, NetflixPurchesedPrice * .8] 
# PRICE_high=[ApplePurchesedPrice * 1.3, AmazonPurchesedPrice * 1.3, NetflixPurchesedPrice * 1.3]
PRICE_low=[50,40,30] 
PRICE_high=[100,80,120]
index=0


# stock_bought=[100,200,95]   
# stock_today=[80,30,120]  
    

class StockTrade(KnowledgeEngine):

  
    
    @Rule(NOT(Fact(x=W())))
    def init(self):
    	print("here")

    @Rule(Fact(x=P(lambda x: x >= PRICE_low[index]) & P(lambda x: x <= PRICE_high[index])))
    def pr(self):
        print("the price is between low and high value, hold the stock") 
        print(PRICE_low[index])
        print(PRICE_high[index])
     
    
    @Rule(Fact(x=P(lambda x: x > PRICE_high[index])))
    def ph(self):
        print("the price is increase by more than 20%, sell the stock ")
        print(PRICE_low[index])
        print(PRICE_high[index])
 #       self.retract(0)
 #       self.declare(Fact(x=50))
         
    @Rule(Fact(x=P(lambda x: x < PRICE_low[index])))
    def pl(self):
        print("the value is less than 50, sell the stock to lock the lost") 
        print(PRICE_low[index])
        print(PRICE_high[index])
        

    
# for i in range(0, 3):
#     print( "start the engine" )
#     index=i
#     print(index)
   
#     print(stock_bought[i])   
#     print(stock_today[i])
#     engine = StockTrade()
# ##    engine.set_averagepurchase_price(100)
#     engine.reset()
#     engine.declare(Fact(x=stock_today[index]))
#     engine.run() 
#    index=index+1
    
       

#for x in range(0, 3):
#   print( "start checking the price" )
#    print(stock_bought[x])   
 #   print(stock_today[x])


class Agent:
	# stocks = [StockTrade(), StockTrade(), StockTrade()]

	def __init__(self, percept):

		# Sensor
		Agent.crawler = WebCrawler('Group 8 AI Project', percept, 'https://investopedia.com')

		# Check the info on the crawler
		# print(Agent.crawler.project_name)

		# States / Knowledge
		
		'''
		Stocks array:[0] = apple
					 [1] = amazon
					 [2] = netflix
		'''
		

		# Stocks to find
		model = {'AAPL', 'AMZN','NFLX'}



		# Agent.rules = StockTrade()

		# Actuators, actions will be based on these variables
		# Agent.decision = 'nothing'
		# Agent.news_score = 0



	# Agent Program function.
	def program(percept):
		action = None



		return action


		# if program is None or not isinstance(program, collections.Callable):
		# 	print('Program has not been specified.')
		# Agent.program =program
	def rule_match(self, state):
	
		for i in range(3):
			# self.stocks[i].setPurchesedPrice(state[i][0]) #price
			index = i
			print(index)
			e = StockTrade()
			print("Start Engine")
			
			e.reset()

			print("Todays Price" + str(state[i][0]))
			e.declare(Fact(x = state[i][0])) #Close price
			e.run()






'''

a = Agent('investopedia.com')
state = [[48], [36], [100]]
for i in range(3):
			# self.stocks[i].setPurchesedPrice(state[i][0]) #price
			index = i
			print(index)
			e = StockTrade()
			print("Start Engine")
			
			e.reset()

			print("Todays Price" + str(state[i][0]))
			e.declare(Fact(x = state[i][0])) #Close price
			e.run()

'''

















