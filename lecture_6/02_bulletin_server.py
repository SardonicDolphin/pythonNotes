#02_bulletin_server

# What you just saw is called a client.
# The client is the program that starts a connection.
# The program that receives the connection is a server.
# The server we contacted is a website.
# We knew that it was waiting on port 80.
# How can we make our own server do that?
# We still need a socket.
# To be extra safe, let's also handle the socket errors,
# whose type we get from the constant error
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, error

try:
	server = socket(AF_INET, SOCK_STREAM)
	# There's a bit more boiler plate here.
	# Servers ideally run forever, but if we close it, or there's an error,
	# we don't want it to still hog the port.
	# Just to be sure, we make the port reusable.
	server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

	# But this time, we are not connecting anywhere.
	# Instead, we tell it where to wait, using the bind method,
	# instead of connect.
	# Now I chose a high port,
	# because you need to be the administrator
	# to use port numbers below 1024.
	server.bind(("", 9001))
	# Notice that I just gave it an empty string for the host name.
	# That means that anybody who can reach this computer
	# can reach this program.
	# If you're on Columbia, that means everybody in the world,
	# who has in internet connection.
	# Let's start listening.
	# If you're following along, you can run 03_bulletin_client.py
	# We also need to put a limit on the number of client connections
	# that we want to keep waiting.
	server.listen(4)
except error:
	print("Setup failed")
	exit(-1)

# You'll need to know my IP address, which I can look up with ifconfig.
# What's the port?

# The limit is pretty small. Can we handle everything you throw at me?
# Yes. Any connections I accept will not count for the limit.
# And if I do things right, you don't have to wait long
# to get accepted.

# We'll need to keep track of all the sockets.
# That's because we'll have multiple sockets,
# and we need to handle them all at once.

sockets = [server]

try:
	while True:
		# You use accept to accept client connections,
		# and give you a new socket,
		# and recv to read messages from the new socket.
		# But both of those wait until you have something.
		# If you just pick a socket and wait,
		# you might be waiting too long,
		# and we'll hit the limit we set for listen really quickly.
		# So we use select.
		# It let's you choose the next socket that's ready,
		# so you don't have to just wait for one event.
		# Actually, for Linux and Mac OS X, it works for files, too.
		# But we only care about reading network sockets,
		# which works for all operating systems.
		from select import select
		# We don't care about writes and errors
		reads, writes, errors = select(sockets, [], [])
		for read_socket in reads:
			# Remember we put the server in the list,
			# so if the server is ready to accept,
			# we will get exact same object,
			# so it's safe to use "is"
			if read_socket is server:
				# We accept and remember any
				# incoming connections.
				# We get both a socket to talk to the client,
				# and the IP address or host name of the client.
				try:
					(client_socket, client_host) = \
					server.accept()
				except error:
					print("Accepting failed")
					continue
				# client_host is always a tuple,
				# and the first part is always
				# the host name or IP.
				print("Incoming connection from %s" %
				      (client_host[0]))
				# We save the accepted socket,
				# because we need that to talk to the client.
				# The server socket is only for
				# listening for new connections
				sockets.append(client_socket)
			else:
				# For client sockets, we read data.
				# We need to get as much of the message
				# as we can.
				# Again, we only get bytes.
				message_bytes = b""
				# We don't know how long the message will be,
				# ahead of time, so let's keep reading until
				# there is nothing left.
				# Notice that we have to say
				# how much we want to read ahead of time.
				reading = True
				while reading:
					LIMIT = 4096
					try:
						new_bytes = \
						read_socket.recv(LIMIT)
						message_bytes += new_bytes
						# We know we ran out
						# if we get less than
						# we asked for.
						reading = len(new_bytes) == \
							  LIMIT
					except error:
						print("Reading error")
						reading = False
				# As I said, everything's in raw bytes.
				# To convert it to a readable string,
				# we decode it.
				message_str = message_bytes.decode()
				if (len(message_str) > 0):
					print(message_str)
					# Let's try some things that don't work,
					# because the errors can show up
					# unexpectedly.
except KeyboardInterrupt:
	print("Cleaning Up")
	# Clean up everything.
	for socket in sockets:
		socket.close()

# Now if I set the host name to "localhost", or 127.0.0.1,
# then only I can connect to it.
