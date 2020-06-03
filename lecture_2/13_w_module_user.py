# So we can use a module in other files.
# For example, in the console. It works the same way as a script.

# You can import the module. Just give the name, without the ".py"
import module
# Let's look what's inside.
dir(module)

# Also, we can see the documentation.
print(module.__doc__)

# Let's see what the variable is.
# You access the member with a dot.
module.MODULE_VAR

# Let's run the function
module.module_function(1)

# But what if you don't want to always have that "module." in front?
# You can import the members directly.

from module import MODULE_VAR
MODULE_VAR

# You can import multiple variables at the same time
from module import module_function, MODULE_VAR_2

# Or you can import everything directly underneath it
from module import *
module_function(0)
# It makes programming easier, but reading harder,
# because somebody else reading your code
# will not see where a variable is from.
