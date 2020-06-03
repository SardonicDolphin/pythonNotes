#03_bulletin_client

# So let's try the client.
# It's a lot like the one for web, except it's to a different host and port.

from argparse import ArgumentParser

parser = ArgumentParser(description = "A simple messaging client")
parser.add_argument("host", help = "Host name or IPv4 address")
parser.add_argument("name", help = "Your user name")
parsed_args = parser.parse_args()

from socket import socket, AF_INET, SOCK_STREAM, error

# This is the same as the first client.
client = socket(AF_INET, SOCK_STREAM)
try:
	# The server might not be available.
	# Here's a case you might get an error.
	client.connect((parsed_args.host, 9001))
except error as se:
	print("Connecting error: %s" % (se))
	exit(-1)

# What's different is how we generate the message.
message = input("Message: ")
full_message = "%s said: %s" % (parsed_args.name, message)
# We're getting strings, but we need bytes. So we encode the string to bytes.
try:
	client.send(full_message.encode())
except error:
	print("Writing error")

# Let's be nice and close, again.
client.close()
