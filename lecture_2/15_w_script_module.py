# So you when you import the module,
# it will run it as a script.
import module_script
quit()
# Even if you import a specific variable.
# It still has to execute everything to make sure the variables
# are properly assigned.
from module_script import do_nothing
# So how can we avoid running the script part?
