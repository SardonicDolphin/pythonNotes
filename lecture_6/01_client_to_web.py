#01_client_to_web

# Up to now, we've been mostly talking about programming techniques,
# and how to handle simple files that you might find on your computer.
# Today, I'll talk about how your program can talk with other programs,
# and how to parse some more complex kinds of files that you see every day.

# You can make your program talk to other programs,
# even if they're on other computers.
# Your web browser does that all the time, using the internet.
# Let's start off with a little about how networked applications work.
# Say we want to go to look for courses on the CS website.
# This is the URL:
# http://www.cs.columbia.edu/education/courses/#
# It has four parts. The scheme, the host, the path, and the fragment.
# The scheme, or the protocol, comes before "://". Here, it's HTTP.
# Next comes the host, whose name is www.cs.columbia.edu.
# Then comes the path, which starts from the first slash
# after the host, and is /education/courses/.
# It looks a lot like paths you would see on a Linux or Mac.
# Finally, you see a hash, followed by a blank string.
# The fragment is optional --you don't even need to write the hash.

# Let's look more closely at each part.
# The host is the computer that is hosting the website.
# It can be a bunch of names separated by dots, like here, or an IP address.

# But I don't want to talk just to any program on the server.
# Besides, I want to know what protocol I want to use.
# For that reason, the host splits network connections into ports.
# Those are numbers that each program can reserve,
# so that it can get messages intended for that port.
# For HTTP, the port is 80 by default, so we don't usually have to type it
# on your browser.
# Now, we have everything we need to know make a connection.

# In most operating systems, your program needs a socket
# to be able to talk over the network.
# We also need to tell it which protocols we will need to find the other host,
# and which kind of port we want to use.
# We will be using something called IPv4, and TCP.
# IPv4 is the most common IP protocol for contacting
# other computers over the internet.
# That's represented by the constant AF_INET.
# TCP automatically makes sure your messages are reliably sent.
# It's slower than something called UDP, which is not reliable,
# but for most Python programs, TCP is good enough.
# The constant you want to use for TCP is SOCK_STREAM.

from socket import socket, AF_INET, SOCK_STREAM

# So, let's put it all together, and make a socket.
s = socket(AF_INET, SOCK_STREAM)
# Now we want to contact the server.
# We need the host name, and the port.
# We know from the URL that the host name is www.cs.columbia.edu.
# And the HTTP protocol's port is 80.
# We pass them both as a tuple to the connect methed.
s.connect(("www.cs.columbia.edu", 80))

# Now we send our request.
# You won't have to remember too much about this the contents,
# except that we're just sending the path.
# The hash is just for browser to handle.
# Also notice that I am sending bytes, with "b" in front of the string.
# This is a Python 3 thing. Strings and bytes are not the same.
# Strings also support unicode, which can be larger than 255,
# but bytes can only be at most 255.
s.send(b"GET /education/courses/ HTTP/1.1\nHost: www.cs.columbia.edu\n\n")
# Now we get a reply, with recv
result = s.recv(128)
# The results are also in bytes, and we have to say how much we want.
# Let's see what we have.
print("Server replied with")
# As you can see, we got bytes as a result.
print(result)

# Now, let's play nice and close the socket.
# That also tells the other side that we are done.
s.close()
