# In the documentation, you will see an optional argument called "shell".
# What it does is make your terminal program run the string you give it.
# Don't ever use it. It's slow because it will use shell.
# And it's insecure, especially when the user can affect the arguments.
# In the terminal, you can type multiple commands on one line,
# and separate them with a semicolon.
# You can give any command line argument by just putting it in quotes,
# like a string in code.
# So after the semicolon, you can put a full command.
# If shell is True, you can do the same thing.
# Let's try "attack; firefox https://xkcd.com/327"

from subprocess import Popen, PIPE
from argparse import ArgumentParser

parser = ArgumentParser(description = "Copy file out")
# This time we let the user control the output file.
parser.add_argument("outfile", help = "output file")
parser.add_argument("--infile",
		    help = "input file, instead of a default string",
		    action = "store")
results = parser.parse_args()

if (results.infile is None):
	in_stream = PIPE
else:
	in_stream = open(results.infile, "r")

command = "dd of=" + results.outfile
print("Running %s" % (command))
# When shell is True, you just give the command as one string.
process = Popen([command], stdin = in_stream,
		shell = True)

if (results.infile is None):
	process.communicate(b"default")

status = process.wait()
print("status: %d" % (status))
