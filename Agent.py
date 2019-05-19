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
from WebCrawler import *
from Memory import *
from KnowledgeBase import *
import collections

class Agent:
	def __init__(self, page_url, program=None):

		# Sensor
		Agent.crawler = WebCrawler('Group 8 AI Project', page_url, 'https://investopedia.com')

		# Check the info on the crawler
		# print(Agent.crawler.project_name)

		# States / Knowledge
		Agent.rules = StockTrade()

		# Actuators, actions will be based on these variables
		Agent.decision = 'nothing'
		Agent.news_score = 0


		if program is None or not isinstance(program, collections.Callable):
			print('Program has not been specified.')
		Agent.program =program



'''
	Might be needed: Knowledge based agent.

'''



'''
	#################################################################
	Agent program similar to the model based agent program.
	#################################################################

	Similar to the pseudocode in the book.

	Notes about this function:
		1. Program is actually a collection.Callable variable; so it will be able to hold
			numerous types of data.
			rule.action may also be a collection/Callable variable; will have to check the RBR later ******

'''
def WebCrawlerAgent(percept):
	def program(percept):
		program.state = update_state(program.state, program.action, percept, model)
		rule = rule_match(program.state, rules)
		action = rule.action
		return action
	program.state = program.action = None
	return program


'''
	Rule matching algorithm; will be used once the algorithm has been 
	implemented, finding the rule that matches the state and then returning the
	action for the agent to perform.

	Variables:
		1. State: the current percepts of the web crawler  (Might be an array of json / collections)
		2. Rules: Rules from the RB-Representation to check

'''
def rule_match(state):
	kb = Agent.rules
	kb.reset()
	for s in state:
		kb.declare(Fact(x = s))
		kb.run()




'''
	##########################################################################################
		Update_state function

		Variables:
		1.  state:  The current state of 
	##########################################################################################
'''
def update_state(state, action, percept, model):
	return


















