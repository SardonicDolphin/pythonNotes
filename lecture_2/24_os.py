# I'll end off the day, and my talk about files,
# with a module that will help you search and organize.
# It's called os.
# Actually, it gives you access to a lot of operating system features,
# which is why it's called os. But I'll focus on files.
import os
print("The module os has attributes: %s"%(dir(os)))
# So, as you can see, there is a lot of stuff.

input()
# It has some operating-specific constants.
# Like the path separators, with os.sep.
# What do you think this would be here?
# What about Windows?
# That is a minor reason for using a virtual machine.
# But if you use sep, instead of whichever slash you normally use,
# this should not be a problem.
print("Segments in a path are separated by %s"%(repr(os.sep)))
# Or the placeholder for the current directory, with os.curdir
print("The current working directory can be accessed with %s"%(repr(os.curdir)))

input()
# What is the current working directory, actually?
# os also gives you the process's current state,
# like the actual path to the current working directory.
# os.getcwd is not a constant, but a function.
print("The current working directory is %s"%(repr(os.getcwd())))

input()
# Let's say you want to start searching for files in a directory.
# There is os.listdir, where you give the directory path,
# and it lists everything in that directory
DIRECTORY = "super_module"
print("Entries in directory %s %s"%(DIRECTORY, os.listdir(DIRECTORY)))
# Notice that it only gives you the names.
# So it's up to you to find the full path,
# by concatenating the directory, the separator, and the name.
# If you want to find all of the files in the directory,
# even those not directly under this one,
# you could try recursion.
# That's helpful if the path to a file will affect what the function will do.
# But first, what do we need for recursion?
# What's the base case? What's the recursive case?

# To help you with that,
# you can use more interesting functions in the submodule, path.
# You can actually see it in dir(os), because it's the name that it assigned
# to another module that it imported.
# Now if we wanted to import path directly,
# we might have some trouble.
# What if we already imported sys.path?
# Luckily, in Python, you can rename a module that you import.
# Just use "as" after the object that you import.
input()
from os import path as os_path
# Let's look inside.
print("The module os.path has attributes: %s"%(dir(os_path)))

# We have a bunch of functions starting with is*,
# which check if a path is a certain type.
# In particular, we have isdir, and isfile,
# to check if the entry is a directory, or a simple file.

# So if we can use listdir recursively,
# what should we use for our base case or recursive case?
# For example, let's write a function that prints out all of the files
# in a directory,
# but the deeper you are, the more the output is indented
# Let's import the functions directly
from os import listdir
from os.path import isdir
# We'll also need the separator between the parts in the path
from os import sep

def print_files(root, depth = 0):
	"""print_files(root[, depth])
Prints the files in the current directory,
with the top level indented with the given depth, which is 0 by default.
root: the root of the current directory
depth: the top-level indentation depth"""
	# Print the current path, with indentation
	print("  " * depth + root)
	# Base case: Not a directory, so stop.
	if (not isdir(root)):
		return
	# Recursive case: Print the children entries
	# Let's make sure to put a separator at the end.
	if (len(root) > 0 and root[-1] != sep):
		root += sep
	entries = listdir(root)
	for entry in entries:
		entry_path = root + entry
		print_files(entry_path, depth + 1)
input()
# Let's try it here. Start with the default depth.
print_files(os.curdir)

# What if we wanted the full path in this case?
# But what if we wanted to get the full path in a directory
# for which we only know the relative path, like super_module?
# but we don't want to put together the paths ourselves?
# os.path has realpath, which does the translation for us.
input()
print_files(os_path.realpath("super_module"))

# But most of the time, you just want to go through all of the files.
# os has another function, called walk.
# The nice thing is, it even has a separate list for directories,
# even though walk made the distinction less necessary now.
# So let's just try printing all of the paths.
from os import walk

input()
for dirpath, dirnames, filenames in walk(os.curdir):
	# We just want to print all of the file paths.
	# We print a directory as we traverse it.
	if (len(dirpath) > 0):
		dirpath += sep
	print(dirpath)
	# To get the path, just add the directory path in front
	paths = map(lambda name: dirpath + name, filenames)
	for path in paths:
		print(path)
