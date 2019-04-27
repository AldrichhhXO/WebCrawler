from Memory import *

"""
	Spider Implementation.

"""
class YungSpider:


	# Name of the folder containing the files
	project_name = ''
	base_url = ''
	domain_name =''

	'''
		Set that will determine what has been crawled and what
		needs to be crawled.

	'''
	queue = set()
	crawled = set()

	# Called when spider is created.
	def __init__(self, project_name, base_url, domain_name):

		# Initialization of the Yung Spider.
		print("Initializing")
		self.project_name = project_name
		self.base_url = base_url
		self.domain_name = domain_name
		self.setup()

	# Sets up the web crawler.
	def setup(self):
		create_project_dir(self.project_name)
		
		