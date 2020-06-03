print("Printing from a range")
for index in range(10):
	print("Range contains %d"%(index))

list_to_loop = ["a", "b", "c", "d", "e", "f"]
input("Printing from the list: %s"%(list_to_loop))
for element in list_to_loop:
	print("List contains: %s"%(element))

input("Searching from the list, and exit using \"break\"")
for element in list_to_loop:
	print(element)
	if element == "c":
		print("Found it!")
		break

input("Skipping over the rest of the loop body, using \"continue\"")
for element in list_to_loop:
	if element == "c":
		print("Skip it!")
		continue
	print(element)
