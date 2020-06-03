#10_json_requests


# Now let's get to gathering actual data.
# You saw that you can use requests.get.
# Some websites are nice enough to give you an API,
# so you have something that is very easy to parse, like json.
# In fact, one website that does it is Columbia's very own CULPA.
# The documentation is at: http://culpa-team.github.io/api/

from requests import HTTPError, get
from json import loads

# When it comes to web scraping,
# you have to do some exploration on your own,
# and figure out what you can automate.
# So the documentation says you can search classes with
# http://api.culpa.info/courses/search/
# Let's search for Python, using
# http://api.culpa.info/courses/search/Python
# There are actually two classes, but ours has id 5519
# We can get the reviews for a class
# using http://api.culpa.info/reviews/course_id/[course id].
# So we visit http://api.culpa.info/reviews/course_id/5519
# OK. That's a lot of reviews. But who are all the instructors?
# We see the professor ID's, so we can look that up,
# using http://api.culpa.info/professors/professor_id/
# So let's search for http://api.culpa.info/professors/professor_id/11132
# Something tells me this is Ang, who was in the same lab as me.
# And yes, it is.

# Let's automate all that.
# First, ask for a search term.
search_word = input("Enter search words for the course: ")

# If put anything inside a URL, we have to make sure it's properly encoded.
# For that, use quote from urllib.parse
from urllib.parse import quote
search_url = "http://api.culpa.info/courses/search/" + quote(search_word)
search_result = get(search_url)
try:
	search_result.raise_for_status()
	search_json = loads(search_result.text)

	# Let's get the class entry, which is under the key "courses"
	classes = search_json["courses"]
	n_classes = len(classes)
	if n_classes == 0:
		# If we have nothing, just exit.
		print("No results for " + search_word)
		exit(-1)
	elif n_classes == 1:
		# Pick the single result, if that's all there is.
		class_entry = classes[0]
	else:
		# Otherwise, we ask the user for the specific class.
		for class_index in range(n_classes):
			current_class = classes[class_index]
			# We print an option number,
			# and the class name, which is a dictionary entry,
			# with the key "name"
			print("%d: %s" % (class_index, current_class["name"]))
		class_entry = None
		while class_entry is None:
			# We check that it's a number that is not too high.
			choice_str = input("Enter a class number: ")
			if not choice_str.isdigit():
				print("%s is not a number" % (choice_str))
				continue
			choice = int(choice_str)
			if choice >= n_classes:
				print("%d is too high. It must be less than %d"
				      % (choice, n_classes))
				continue
			class_entry = classes[choice]
except HTTPError:
	print("Could not fetch " + search_url)
	exit(-1)

# Now that we got the class, we can get its ID, which is the value
# with the key "id", and we can get its reviews.
# Note that IDs are integers.
class_url = "http://api.culpa.info/reviews/course_id/" + \
	    quote(str(class_entry["id"]))
review_result = get(class_url)
try:
	review_result.raise_for_status()
	review_json = loads(review_result.text)

	# The reviews are under the key "reviews"
	reviews = review_json["reviews"]

	for review in reviews:
		# Getting the date, review and courseload is easy.
		# Just get the "created",
		# "review_text" and "workload_text" entries
		date = review["created"]
		review_text = review["review_text"]
		workload_text = review["workload_text"]

		# We can get the IDs of the instructors,
		# but we also want their names.
		prof_ids = review["professor_ids"]
		prof_names = []
		for prof_id in prof_ids:
			prof_url = \
			"http://api.culpa.info/professors/professor_id/" + \
			quote(str(prof_id))
			prof_result = get(prof_url)
			try:
				prof_result.raise_for_status()
				prof_json = loads(prof_result.text)

				# Let's get the professors list.
				# They really like dictionaries.
				# Mostly a Javascript thing.
				profs = prof_json["professors"]
				# Let's just handle professors with at least
				# one name, and use the first one.
				if len(profs) < 1:
					continue
				prof = profs[0]
				# We get the first and last name,
				# and combine them.
				prof_names.append(prof["first_name"] + " "
						  + prof["last_name"])
			except HTTPError:
				print("Could not fetch " + prof_url)
				exit(-1)

		# Let's print it all out.
		print(date)
		print("\tProfessors: " + ", ".join(prof_names))
		print("\tReview: " + review_text)
		print("\tWorkload: " + workload_text)
		print()

except HTTPError:
	print("Could not fetch " + class_url)
	exit(-1)
