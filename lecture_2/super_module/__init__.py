"""This supermodule includes many modules in its directory.
It's so big, that the comment for this supermodule needs multiple lines."""

# You have to import the submodules to see them in dir,
# although it's not necessary to import them directly.
# Use . to refer to the current directory.
from . import submodule_1, submodule_2

def super_module_function():
	"This function is directly accessible in the supermodule."
	return None
