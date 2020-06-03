#log_messages.py

from logging import debug, info, warning, error, critical

# You can write to the logs at different levels.
# The levels are quite subjective,
# but there is an order of severity,
# which affects whether or not the message will be printed.

# The nice thing is that you can call these functions anywhere,
# and not always have to worry about what will be printed, and to where.

def write_logs():
	debug("Things happening behind the scenes, that might be useful.")
	info("Information about the progress of the program.")
	warning("This is not good, but let the user decide.")
	error("Something that should not happen happened.")
	critical("Like an error, but also not recoverable.")
