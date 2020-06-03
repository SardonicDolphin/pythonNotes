# You will hear about other ways to execute code.
# And you don't really want to use any of them either.

# exec executes anything you give it.
# So you can do anything bad with it.
code = input("Give me some code to execute:\n")
print("Executing\n" + code)
exec(code)

# Sure, it's one line. But that's all I need.
# Remember from the second homework that you can import anything
# given just a string.
# Now we know about a module that lets you run any program.
# So let's try the input:
# __import__("subprocess").Popen(["firefox", "https://xkcd.com/327"])
