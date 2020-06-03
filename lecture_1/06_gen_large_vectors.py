from random import random
from subprocess import Popen

# Unlike other languages, Python is interpreted,
# which is why it can be used without a compiler.
# But it also means your Python program does produce optimized machine code.
# So it's not useful for system and stand-alone programs,
# especiall when performance matters.

LARGE_SIZE = 2 ** 16

def generate_random_array():
	return list(map(lambda x: random(), range(LARGE_SIZE)))

def c_repr(array):
	joined = ", ".join(map(str, array))
	return "{%s}"%(joined)

PYTHON_CODE ="""def dot_multiply_vectors(v_0, v_1):
	total = 0.0
	for element_i in range(len(v_0)):
		total += v_0[element_i] * v_1[element_i]
	return total

print("%.06f"%(dot_multiply_vectors(vector_0, vector_1)))"""

C_CODE = """#include <stdio.h>
#include <stdlib.h>

static double dot_multiply_vectors(double *v_0, double *v_1, size_t vector_len)
{{
	double total = 0.0;
	size_t element_i;

	for (element_i = 0; element_i < vector_len; element_i++) {{
		total += v_0[element_i] * v_1[element_i];
	}}

	return total;
}}

int main(void) {{
	printf("%.06f\\n", dot_multiply_vectors(vector_0, vector_1, {0}));
	return 0;
}}"""

VECTOR_IDS = range(2)
random_vectors = map(lambda _: generate_random_array(), VECTOR_IDS)

def gen_python_assignment(vectors, index):
	return "vector_%d = %s\n"%(index, repr(vectors[index]))

python_source = open("07_slow.py", "w")
for vector_i in VECTOR_IDS:
	python_source.write(gen_python_assignment(random_vectors, vector_i))
python_source.write(PYTHON_CODE)
python_source.close()

def gen_c_assignment(vectors, index):
	return "static double vector_%d[] = %s;\n"%(index,
						   c_repr(vectors[index]))

C_PROGRAM_NAME = "08_fast"
C_SOURCE_NAME = C_PROGRAM_NAME + ".c"

c_source = open(C_SOURCE_NAME, "w")
for vector_i in VECTOR_IDS:
	c_source.write(gen_c_assignment(random_vectors, vector_i))
c_source.write(C_CODE.format(LARGE_SIZE))
c_source.close()

compile_job = Popen(["gcc", "-o", C_PROGRAM_NAME, C_SOURCE_NAME])
compile_job.wait()
