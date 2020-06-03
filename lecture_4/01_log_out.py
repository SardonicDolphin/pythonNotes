#01_log_out.py

# Today I will be talking about some modules that can make programming in Python
# much more simple.
# The first two will be useful when you want to create reliable programs.
# The last one is a feature that makes Python useful for parsing
# arbitrary text.

# When something goes wrong in a program, you want to know what's going on.
# One easy way to do that is by logging.
# You might have been putting around prints in the code,
# when you want to track what is going on.
# But you don't always want that printing in your code
# when people are actually using it.
# And if you do, you might want to print it elsewhere.

from log_messages import write_logs

from logging import basicConfig, DEBUG, INFO, WARNING, ERROR, CRITICAL

# basicConfig lets you set the configuration, but it's optional.
# By default, it prints to standard output with the level at WARNING,
# so that every message at WARNING or above is printed.
print("Default:")
write_logs()

# Here's a little reset routine so that I can change settings.
# You don't usually need this, unless you want to change the logging setting
# during runtime.

from logging import root

def reset_settings():
	for handler in root.handlers:
		root.removeHandler(handler)

input()
# We can also set different levels.
# Let's go from the least severe to the most severe.
print("Debug level:")
reset_settings()
basicConfig(level = DEBUG)
write_logs()

input()
print("Info level:")
reset_settings()
basicConfig(level = INFO)
write_logs()

input()
print("Warning level:")
reset_settings()
basicConfig(level = WARNING)
write_logs()

input()
print("Error level:")
reset_settings()
basicConfig(level = ERROR)
write_logs()

input()
print("Critical level:")
reset_settings()
basicConfig(level = CRITICAL)
write_logs()


input()
# We don't have to print to standard output.
# We can also write it to a file.
print("Regular file output")
reset_settings()
# Anybody know what this will print?
basicConfig(filename = "log", level = WARNING)
write_logs()

input()
# Normally, if I write to the same file again,
# it'll keep the old data.
# Say we want to print only critical messages this time
print("File output with critical level, only")
reset_settings()
# What will this print?
basicConfig(filename = "log", level = CRITICAL)
write_logs()

input()
# When you write to files, what mode would you use to overwrite the file?
# You can also use it here.
print("Overwriting file with critical level, only")
reset_settings()
# What will this print?
basicConfig(filename = "log", filemode = "w", level = CRITICAL)
write_logs()

input()
# Don't like the output format? What about some other information, like time?
print("Using formatting")
reset_settings()
basicConfig(level = WARNING, \
	    format = "%(levelname)s at %(asctime)s:%(message)s")
write_logs()

input()
# If you're wondering how this works,
# it's because if you format with a dictionary,
# you can access values with string keys
# by mentioning their names in parentheses
print("This has been formatted with %(datastruct)s"%{"datastruct":
						     "dictionaries"})
