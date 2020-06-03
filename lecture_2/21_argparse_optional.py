# Like with functions, you can also add optional arguments,
# which the user can arbitrarily insert.

from argparse import ArgumentParser

# Let's create the parser again, with a required argument
parser = ArgumentParser(description = "A more complicated script, " +
				      "with optional options")
# Just the bare bones for the required argument this time.
# By default, it is of type string.
parser.add_argument("required")

# Add a basic, optional argument, starting with two dashes.
# If the default value is not given, it is None
parser.add_argument("--basic", help = "integer, with no default",
		    action = "store", type = int)
# Add an optional argument with 0 being the default value.
parser.add_argument("--defaulted", help = "integer value, with default",
		    action = "store", type = int, default = 0)
# Add an optional argument with a shortcut, starting with a single dash.
parser.add_argument("-s", "--shortcut", help = "stores a string value",
		    action = "store")
# Add an optional flag that stores the corresponding variable to true, if set.
# It requires no explicit value.
# The opposite is value is used for "store_false"
parser.add_argument("--boolean", help = "sets a boolean value",
		    action = "store_true")

parse_result = parser.parse_args()

# The required argument, again, but this time a string.
print("Required value: %s"%(parse_result.required))

# The attribute name is the option name with the two dashes removed.
# The "basic" option displays None if it is not given
print("Basic option: %s"%parse_result.basic)
# This option gives the explicit default value, if no value is given.
print("Default option: %d"%parse_result.defaulted)
# This option is available if you give the full name, or the shortcut.
print("Shortcut option: %s"%parse_result.shortcut)
# This option is false if not given, true otherwise.
print("Boolean option: %s"%parse_result.boolean)
