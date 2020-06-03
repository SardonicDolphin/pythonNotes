# We've been using the terminal so much.
# But only with Python.
# There are so many other programs, too.
# For example, let's say you want to know the IP addresses of your computer.
# There is hostname.
# If you want to know what hostname does, just type "man hostname".
# This is a manual page, or man page for short.
# You can get the man page for almost any program you have installed.
# Anyways, if we look at the man page for hostname,
# you see that you can get all IP addresses with -I.
# Let's see what that looks like.
# So you get a list of all non-local IP addresses.
# Let's say we want to use it in Python, so that we can process it more.
# How do we run the program, and how do we get the output?
# We use the subprocess module.

from subprocess import Popen, PIPE

# Popen is a class, and you start the process by initializing an object
# The only argument you always need is a list of arguments.
# It's like the argv to the program, so it includes the program,
# as well as any options.
# Because we expect output, we also set the stdout argument to PIPE
process = Popen(["hostname", "-I"], stdout = PIPE, stderr = PIPE)

# Now we can get the results.
# communicate lets you get the results at the end.
# It's not so helpful if you want to get anything in the middle.
# It returns the output and error text.
# If we didn't set the parameters to PIPE,
# their respective values would be None.
out, err = process.communicate()
print("Have %d bytes from the standard input stream, " % (len(out)) +
      "and %d bytes from the standard error stream" % (len(err)))

# You can use poll to check if it has finished.
# If it has, which is always true in this case,
# it will return the exit number.
# Every program does that. In Python, it's usually 0,
# unless you call exit with a number.
# There is another method called wait,
# which waits for the end, but you usually don't want to use that
# if you read from the program,
# because then the program will wait for Python,
# and Python will wait for the program.


# So now we can get the IP address
# Be careful about Python 3. It doesn't return a string,
# so you have to decode it into a string.
# For example, the encoding I've been using so far is UTF-8.
print("Output is of type %s" % (type(out)))
out_str = out.decode("UTF-8").rstrip()
ips = out_str.split(" ")

print("Your IP addresses are:")
for ip in ips:
	print("\t" + ip)
