# You won't need to know this for the homework,
# but it's pretty useful for the project,
# because you'll need to get more organized.
# You can have a directory of modules.

# Let's look at the folder super_module.
# It has an __init__.py file, which says that this folder is a module.
# But you also have some other ".py" files. Those are the submodules.
# Let's look at the main module.

# Let's use it
import super_module
dir(super_module)
# We have this function
print(super_module.super_module_function.__doc__)

# You import the submodule like any other object
from super_module import submodule_function

# And you can also import objects inside the submodules,
# by pretending that you are accessing the submodule,
# with the dot syntax.
from super_module.submodule_1 import submodule_function

# But sometimes, you have a module in another directory,
# and the directory doesn't have the __init__.py file.
# Luckily, there is a module for that. sys.path
from sys import path
# It's a list of all the paths in which Python looks for modules.
print(path)
# You can see the empty path, which is the current directory,
# and also some standard directories.
# Let's say we have a module in the directory "other_directory".
# We can add the directory.
path.append("other_directory")
# Now we can import the module
import other_directory_module
