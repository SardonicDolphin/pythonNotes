#09_auto_parse_bot

# Now let's put all the robots code into one single, automated function.
# There is one piece missing?
# How do we figure out where robots.txt is?
# We can get the scheme and host name from the URL,
# and put in robots.txt for the path.
# To do that cleanly, we use urllibs.parse

from urllib.parse import urlsplit, SplitResult, urlunsplit

# I mentioned how the URL has many parts.
# We need to split them to properly replace the path.
def to_robots(url):
	split_url = urlsplit(url)
	# To put it back together,
	# we need to create a new SplitResult.
	# We need the scheme, which is the protocol,
	# the host name, which is called netloc,
	# the path, the query string, and the fragment.
	# But the query string and fragment are empty,
	# and we know that the path is always robots.txt.
	split_robots_url = SplitResult(scheme = split_url.scheme,
				       netloc = split_url.netloc,
				       path = "robots.txt", query = "",
				       fragment = "")
	# And we put it together, using urlunsplit.
	return urlunsplit(split_robots_url)

from requests import get, HTTPError

# Let's also put the crawl delay finding in a nice, clean function.
# We'll use this to find the start and end of the user agent commands.
# We also use it to check if the agent even exists.
# If not, there are no rules for that particular agent.
AGENT_STR_START = "User-agent: "
# Define the crawl delay command, so we can reuse it
# for finding it at the beginning, and where it ends.
CRAWL_DELAY_STR = "Crawl-delay: "
CRAWL_DELAY_START = len(CRAWL_DELAY_STR)
def get_delay(user_agent, robots_url):
	bot_request = get(robots_url)
	try:
		# Mostly a repeat
		bot_request.raise_for_status()
		bot_text = bot_request.text
		bot_lines = bot_text.split("\n")
		found_agent = False
		# But customized for each agent
		for bot_line in bot_lines:
			if bot_line == AGENT_STR_START + user_agent:
				found_agent = True
			elif found_agent:
				if bot_line.startswith(AGENT_STR_START):
					break
				elif bot_line.startswith(CRAWL_DELAY_STR):
					delay_str = bot_line[CRAWL_DELAY_START
							     : ]
					if delay_str.isdigit():
						return int(delay_str), True
					else:
						break
		return 0, found_agent
	except HTTPError:
		return 0, False

from urllib.robotparser import RobotFileParser

# Now, putting it all together, we check if we can fetch the URL,
# and if so, return the delay. Otherwise, return None
# Remember the wildcard for checking fetchability and delay
GENERAL_AGENT = "*"
def check_delay(user_agent, url):
	robots_url = to_robots(url)

	# Fetch the delay for all programs, ond this one in particular.
	general_delay, have_general = get_delay(GENERAL_AGENT, robots_url)
	agent_delay, have_agent = get_delay(user_agent, robots_url)

	# The next part is straightforward:
	# Check the general rules, and then check the program's rules,
	# if there are rules.
	robots_parser = RobotFileParser(robots_url)
	robots_parser.read()
	if (have_general and not robots_parser.can_fetch("*", url)):
		return None
	if (have_agent and not robots_parser.can_fetch(user_agent, url)):
		return None

	# Use the larger delay.
	if general_delay < agent_delay:
		return agent_delay
	else:
		return general_delay

# You can use this as a module for your homework,
# but let's also make it a script, so that I can show it here.
from argparse import ArgumentParser

if __name__ == "__main__":
	arg_parser = ArgumentParser(description = "Check robots.txt for URL")
	# We always need the URL.
	arg_parser.add_argument("url", help = "The URL to check")
	# The agent is optional, and is the wild card by default
	arg_parser.add_argument("-a", "--agent",
				help = "The user agent to check",
				default = GENERAL_AGENT)

	parsed = arg_parser.parse_args()

	delay = check_delay(parsed.agent, parsed.url)
	if (delay is None):
		print("%s cannot fetch %s" % (parsed.agent, parsed.url))
	else:
		print("The delay of %s for user %s is %ds" % (parsed.url,
							      parsed.agent,
							      delay))
