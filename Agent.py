"""

	This will be the implementation of the agent class

	Based on the sample code from chapter 2. (http://aima.cs.berkeley.edu/python/agents.py);

		1. Object	# Physical object that can  exist in an environment
			- Agent  

		2. Environment # Holds objects; runs simulations

"""



''' 
	Template for the agent class.


	variables:
		- page_url: which will basically describe the environment.
		- stocks_set: Which will hold info on the stocks to view.

	Self initialization:
		- action: The action for the agent to do
'''
class Agent():
	def __init__(self, page_url, stocks_set):
		self.page_url = page_url
		self.stocks_set = stocks_set
		self.percept_sequence = []
		self.action = 'Power up'


	def get_percep()


