# What if you want to send input?
# Other programs also have a standard input stream.
# You can do it from two sources.
# Directly from a file, or from a string.

from subprocess import Popen, PIPE
from argparse import ArgumentParser

# For example, let's use the dd program.
# It lets you copy between two file streams.
# By default, the file streams are the standard ones.
# But let's output to an actual file.

parser = ArgumentParser(description = "Copy file out")
parser.add_argument("--infile",
		    help = "input file, instead of a default string",
		    action = "store")
results = parser.parse_args()

# Let's use a default string. Otherwise, use the given file.
if (results.infile is None):
	# If you want to input data directly,
	# you can use communicate.
	in_stream = PIPE
else:
	# Otherwise, you can use a file.
	# You need the binary mode, though.
	in_stream = open(results.infile, "rb")

process = Popen(["dd", "of=dd_out"], stdin = in_stream)

# By default, we use communicate
if (results.infile is None):
	# Python 3 requires that this be a byte buffer.
	# So encode this time.
	process.communicate("default".encode("UTF-8"))

# Now we don't read any output, so we can just use wait()
status = process.wait()
print("status: %d" % (status))

# Close the file at the end.
if (results.infile is not None):
	in_stream.close()
