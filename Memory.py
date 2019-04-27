import os

"""
	This file will be responsible for keeping track of the crawled 

"""

# Each website you crawl is a separate project (folder)
def create_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating project ' + directory)
		os.makedirs(directory)

# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')

# Create a new file
def write_file(path, link):
	f = open(path, 'w')
	f.write(link)
	f.close()

# Adds a new link to crawl.
def addData(path, link):

	# 'a' is Append mode
	with open(path, 'a') as file:
		file.write(link + '\n')

# Delete The contents of a file
def delete_content(path):
	with open(path, 'w'):
		pass	# do nothing

# Using a set to keep the crawled/queued files unique, skipping the crawls.

# Read a file and convert each line to set items.
def convert_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results

# Convert a set to a file
"""
	first deletes the old data
	Then inserts updated data.
"""
def convert_to_file(links, file):
	delete_content(file)
	for link in sorted(links):
		addData(file, link)

# create_data_files('stocks', 'https://www.investopedia.com')








# create_project_dir('stocks')