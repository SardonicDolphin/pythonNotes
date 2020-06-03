# 05_other_codes

#If you've visited any website,
# you probably know that not everything goes perfectly.
# Like if I go to https://github.com/thiscannotpossiblyexist.
# Github is an actual website, and I'm using the right protocol,
# but the path does not exist.
# So I get a message that says that I'm wrong.
# You've seen this code before: 404.
# If you look at the network log on your browser, you'll also see 404.

from http.server import HTTPServer, BaseHTTPRequestHandler

# Let's create a server that handles different statuses.
class CodeRequestHandler(BaseHTTPRequestHandler):
	# Here's the normal case.
	def __handle_200(self):
		self.send_response(200)
		self.send_header("Content-Type", "text/html")
		self.end_headers()
		message = """<html>
<head><meta charset="UTF-8"><title>Got Your Contents Right Here</title></head>
<body>
It works!
</body>
</html>"""
		self.wfile.write(message.encode("UTF-8"))
	# If something is missing,
	# you can still give content --usually a short error message.
	# But the response status has to be different.
	def __handle_404(self):
		self.send_response(404)
		self.send_header("Content-Type", "text/html")
		self.end_headers()
		message = """<html>
<head><meta charset="UTF-8"><title>Path Not Found</title></head>
<body>
404 error
</body>
</html>"""
		self.wfile.write(message.encode("UTF-8"))
	# The next code works a little differently.
	# A lot of web pages have alternative names or even host names
	# for the same page,
	# but you obviously don't want to handle them all separately.
	# In that case, use code 302, which is a redirect.
	def __handle_302(self):
		self.send_response(302)
		# There is no content, but you set the Location header
		# to the actual destination.
		self.send_header("Location", "https://google.com")
		self.end_headers()

	# So now let's put it all together in the GET request.
	def do_GET(self):
		# Let's read the path.
		# It always starts with a slash, even if you don't type it.
		# So let's remove it.


# Now let's run the server again.
server = HTTPServer(("", 8080), CodeRequestHandler)
server.serve_forever()

pure_path = self.path[1 : ]

if pure_path in __csvDict:
	self.returnURL = __csvDict[pure_path]
	self.__handle_302()

elif pure_path in __xlsxDict:
	self.returnURL = __xlsxDict[pure_path]
	self.__handle_302()

else:
	 self.__handle_200()
