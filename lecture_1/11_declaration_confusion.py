common_name = "Global value"

def different_scope():
	common_name = "Local value"

print("Before change: " + common_name)
different_scope()
print("After change: " + common_name)
