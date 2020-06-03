#08_delay

# There is a non-standard command
# that you see in a lot of smaller websites,
# called Crawl-delay.
# It can be interpreted many ways,
# but the idea is you should not access the server
# more than once per the number of seconds it gives.
# For example,
# at the CS department's website, at http://www1.cs.columbia.edu/robots.txt

# Unfortunately, robotparser doesn't have anything to parse it.
# So it's up to you to get and parse that information.
# So let's talk about how to parse HTTP data easily.

# There is a module you can download called requests.
# It has a get function, which makes GET requests.

from requests import get, HTTPError

# So let's fetch the robots file.
bot_request = get("http://www1.cs.columbia.edu/robots.txt")
# We need to make sure we got the right result.
# We've seen many status codes that the server can return,
# and more than one of them mean that it's OK.
# The raise_for_status throws an exception if it's not OK.
# Columbia's kind of bad, because it redirects you to the main website.
try:
	bot_request.raise_for_status()
	# We can get the text field, which is already decoded.
	bot_text = bot_request.text
	print("Got data of type %s" % (type(bot_text)))
	# Let's say we want to look for the crawl delay that applies to
	# Slurp.
	# We see lines in the form "User-agent: [user agent]"
	# So we need to look for "User-agent: Slurp".
	# Crawl delay commands are in the form "Crawl-delay: [delay]".
	# So we look for lines that start with "Crawl-delay: ",
	# and parse the rest as an integer.
	# We stop looking for the crawl delay command
	# when we find it, the next agent starts, or there are no more lines.
	bot_lines = bot_text.split("\n")
	found_agent = False
	for bot_line in bot_lines:
		# We look for the commands for the agent Slurp.
		if bot_line == "User-agent: Slurp":
			found_agent = True
		elif found_agent:
			if bot_line.startswith("User-agent: "):
				# If we found the agent already,
				# we stop at the end of the commands.
				break
			elif bot_line.startswith("Crawl-delay: "):
				# Or if we found the delay.
				delay_string = bot_line[len("Crawl-delay: ") : ]
				# We get the number after "Crawl-delay: "
				if delay_string.isdigit():
					crawl_delay = int(delay_string)
					print("Crawl delay is %d" %
					      (crawl_delay))
				else:
					print("Invalid crawl delay string: %s" %
					      (delay_string))
				break
except HTTPError:
	print("Could fetch robots.txt")
