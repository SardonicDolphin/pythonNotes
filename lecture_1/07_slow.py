def dot_multiply_vectors(v_0, v_1):
	total = 0.0
	for element_i in range(len(v_0)):
		total += v_0[element_i] * v_1[element_i]
	return total

print("%.06f"%(dot_multiply_vectors(vector_0, vector_1)))