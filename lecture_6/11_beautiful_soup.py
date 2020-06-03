# 11_beautifulsoup.py

# Now what if the website is not so nice?
# How about two friends are planning a vacation in another country.
# But one is American, and the other is Russian,
# and neither one of them wants to get a visa.
# Let's try Wikipedia.
# We can look up visa requirements for United States citizens.
# And the same for Russian citizens.
# OK. We can kind of eyeball the regions where they overlap.
# But how do we automate this?

# First, we need to know how to reach all of these visa requirement pages.
# Wikipedia is nice enough to have a table at the end.
# The table's actually quite complicated, but if we hover over the links,
# we can see that that all of the article names are in the form:
# "Visa_requirements_for_[country or nationality]".
# If you right click, and inspect the element,
# you see that it's just a path, so it's even easier.
# So we just need to find links.
# How do we do that? With Beautiful Soup.
from requests import get
from bs4 import BeautifulSoup

# I already checked, and robots.txt lets us fetch articles.
# Let's go to a page that includes links to all countries.
START_URL = ("https://en.wikipedia.org/wiki/Template:Visa_requirements")
start_request = get(START_URL)
start_request.raise_for_status()
# Now we can get the HTML text,
# and tell Beautiful Soup to parse it.
start_soup = BeautifulSoup(start_request.text)
# Now: time to search. We want to look for links.
# We use the select method, and just have the tag name as the parameter.
# Remember that "a" stands for link.
links = start_soup.select("a")
# There are quite a lot of links, so we have to narrow it down.
# We can do this quickly with list comprehension.
# We care about the form of the link name.
# So let's create the prefix
LINK_START = "/wiki/Visa_requirements_for"
# We now have to look into the tags.
# What you see there, the href and title, are attributes,
# which the tag stores in the attrs field.
# For links href gives the link destination.
country_links = [link for link in links \
		 if "href" in link.attrs and \
		    link.attrs["href"].startswith(LINK_START)]
# Let's show these tags.
# If you look at them, you notice that there is text outside of the start tag,
# but it is the child of the tag, because the text is surrounded by the
# starting and ending tags. We can get the text, which is more user-readable,
# and map that to the link, which is the value.
country_lookup = {}
for country_link in country_links:
	# We get the text with getText().
	# We get the destination from the attribute href, again.
	country_lookup[country_link.getText()] = country_link.attrs["href"]

# Let's show all of the names. To make life easier, let's alphabetize them.
country_names = list(country_lookup)
country_names.sort() # This sorts the names.
print(", ".join(country_names))

# Getting the information for both countries is very similar.
# So let's put it in a function that asks the user for the coutry name,
# and returns the country's name and visa free countries.
# What kind of data structure should it return for that?

def get_visa_free():
	country_page = None
	while country_page is None:
		country_name = input("Please enter the nationality: ")
		if country_name in country_lookup:
			# Now we can get the URL.
			# But remember, it's just a relative URL.
			# How can we make sure that it translates correctly?
			# In general, we can use urljoin, from urllib.parse.
			# You give it a starting URL, and the link reference,
			# and you get the full URL.
			from urllib.parse import urljoin
			country_link = country_lookup[country_name]
			country_url = urljoin(START_URL, country_link)
			# Now we can fetch the data
			country_request = get(country_url)
			try:
				country_request.raise_for_status()
				country_page = BeautifulSoup(country_request. \
							     text)
			except HTTPError:
				print("Could not fetch %s" % (country_url))
				exit(-1)
		else:
			print("We don't have records for %s" % (country_name))

	# Now we have to get the visa free countries.
	# Tables consist of rows, which have tags <tr>,
	# and their childrens are cells, which have tags <td>
	# Let's get all of them.
	rows = country_page.select("tr")
	# The tables vary for some countries,
	# But we see that the first cell always has the country name in a link,
	# and the second one says if it's visa free.
	visa_free = set([])
	for row in rows:
		# You can get all of the cells, again using select
		cells = row.select("td")
		if len(cells) >= 2:
			visa_cell = cells[1]
			# We check if the "Visa not required"
			# string is in the text that second cell contains.
			if ("Visa not required" in visa_cell.getText()):
				# Now we get the country,
				# which we know is in a link.
				country_cell = cells[0]
				country_links = country_cell.select("a")
				if len(country_links) > 0:
					country = country_links[0].getText()
					visa_free.add(country)
	return (country_name, visa_free)

(first_country, first_visa_free) = get_visa_free()
(second_country, second_visa_free) = get_visa_free()

# Now we take their intersection, and sort it, again.
both_visa_free = list(first_visa_free.intersection(second_visa_free))
both_visa_free.sort()
print("Both %s and %s citizens don't need visas for:" % (first_country,
							 second_country))
for country in both_visa_free:
	print("\t" + country)
