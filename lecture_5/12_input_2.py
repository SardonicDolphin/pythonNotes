# Rather confusingly, in Python 2, input combines raw_input and eval,
# so be careful.
v = input("Please input an expression, which will actually be evaluated:\n")
print "Evaluated %s" % (v)
