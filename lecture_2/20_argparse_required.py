# In Python 3, you can use argparse.
# The current version of Python 2 has it, too.
# Python 2 also has something called getopt, which is similar to C's getopt.
# It's more complicated.

from argparse import ArgumentParser

# Create an argument parser,
# which has a description, for the help message.
parser = ArgumentParser(description = "A simple script requiring one argument")
# Add a required argument, with help text, and of type int
# Can you guess what's really needed here?
parser.add_argument("required", help = "the required argument", type = int)

# Parse the arguments
parse_result = parser.parse_args()

# If we don't enter anything, or enter the wrong type,
# it will give you the error message, and exit.
# It automatically has a help option: -h or --help

# Access the argument as if it were an attribute.
print("Required argument was %d"%(parse_result.required))
