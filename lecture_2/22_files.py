# The next source of inputs is files.
# This is where Python becomes really useful
# for projects that require long-term configuration,
# as well as everyday organization.

# To open a file, you run the open function, with a path, and the mode

FILE_NAME = "out.txt"

def read_out():
	"""\"r\": read only.
We will be reading the output file after each round of writes"""
	print(FILE_NAME + " contains")
	inf = open(FILE_NAME, "r")
	# You can iterate through the file's lines
	for line in inf:
		# Let's look at what bytes are actually in each line.
		print(repr(line))
	inf.close()

# "w": write only
f = open(FILE_NAME, "w")
print("using print", file = f)
# In Python 3, you can pass the file to print
# write lets you write raw data, but with no automatic new line
f.write("using write")
# Don't forget to close. If you don't the script might not save all the data.
f.close()
read_out()

# But be careful! Write mode overwrites the whole file
input()
print("Overwriting")
f = open(FILE_NAME, "w")
print("overwrite", file = f)
f.close()
read_out()

# If you want to keep the old data, use "a" mode for append
input()
f = open(FILE_NAME, "a")
print("append a line", file = f)
print("append another line", file = f)
f.close()
read_out()

# Let's look at some other read operations
input()
inf = open(FILE_NAME, "r")
print("%s object has attributes %s"%(type(inf).__name__, dir(inf)))
input()
# Read lets you read everything at once.
print("read() =")
print(inf.read())
print("read again")
print(inf.read())
input()
# If the file is seekable, that means you can jump to arbitrary parts
# in the file.
print("Seekable? %s"%(inf.seekable()))
inf.seek(0)
input()
# readline lets you read a single line
first_line = inf.readline()
second_line = inf.readline()
print("First line of %d bytes: %s"%(len(first_line), repr(first_line)))
print("Second line of %d bytes: %s"%(len(second_line), repr(second_line)))
# tell tells you where you are in the file
# What do you expect the position to be now?
print("Now we're at %d"%(inf.tell()))
inf.close()
