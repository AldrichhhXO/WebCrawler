from bs4 import BeautifulSoup

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

soup = BeautifulSoup(html_doc, 'html.parser')

# Direct
#  print(soup.body)
# print(soup.head)
# print(soup.head.title)


# Find(), Gets the first one its finds
el = soup.find('div')


# FindAll() or find_all()
# el = soup.find_all('div')
# el = soup.find_all('div')[1]

# el = soup.find(id='section-1')
# el = soup.find(class_='items')
# soup.find(attrs={"data-hello": "hi"})


# Select
# el = soup.select('#section-1')
# el = soup.select('#section-1')[0]
# el = soup.select('.item')[0]

# Get_text(), Gets the text within an element
# el = soup.find(class_='item').get_text()


# for item in soup.select('.item'):
#	print(item.get_text())


# el = soup.body.contents[1].contents[1].find_next_sibling()

# https://www.youtube.com/watch?v=4UcqECQe5Kc


# Navigation
# el = soup.body.contents
# el = soup.find(id='section-2').find_previous_sibling()
# el = soup.find(class_='item').find_parent()

# el = soup.find('h3').find_next_sibling('p') 16:19



print(el)