#07_robots

# Now let's make the client easier, too.
# Before we do that, though, a note about etiquette.
# A lot of websites don't want you just crawling all of their pages
# all the time.
# That's especially important if they have infinite, automatically-generated
# pages.

# They will tell you through the robots.txt file.
# You can check if that exists by taking the URL, and replacing the path.

# You can see the paths that are allowed or not allowed.
# These rules are kind of complicated, but there is a module for that.

from urllib.robotparser import RobotFileParser

# Each parser is associated with a robots.txt file.
# Say for google, we have the scheme, the server name,
# and for the path, it's always robots.txt.
parser = RobotFileParser("https://google.com/robots.txt")
# To be able to use the robots file, you have to read it first.
# This doesn't happen automatically for some reason.
parser.read()

# Now you're ready to go.
# Just use the can_fetch method.
# You give it the name of your program, and the URL you want to fetch.
# You also want to check the rules for all crawlers, using the wildcard, *.
print("Can I fetch \"/\"? %s" % (parser.can_fetch("parser_3101", "/search")))
print("Can anybody fetch \"/\"? %s" % (parser.can_fetch("*", "/search")))
print("Can I fetch \"/search\"? %s" %
      (parser.can_fetch("parser_3101", "/")))
print("Can anybody fetch \"/search\"? %s" % (parser.can_fetch("*", "/")))
