def simple_filter(values):
	"""
	This function takes a list of values as input and prints values which are less than 5.
	"""
	for val in values:
		if val<5:
			print(val)
	
def simple_filter_1(*values, limit=5):
	"""
	This function takes a tuple of values as input and prints values which are less than `limit`.
	"""
	values = tuple(filter(lambda val: val<limit, values))
	print(*values, sep=", ")

def list_filter(limit):
	"""
	This function can be used to generate functions with different filter crietria.
	"""
	def main_filter(*values):
		values = tuple(filter(lambda val: val<limit, values))
		print(*values, sep=", ")
	return main_filter

if __name__ == "__main__":
	my_values = [1,3,12,4,7,31,9,5,20,19,21,100,43,32,71]
	print("Input = {}".format(my_values))

	print("1. simple_filter Output: ")
	simple_filter(my_values)

	print("\n2. simple_filter_1 Output: ")
	simple_filter_1(*my_values)

	print("\n3. simple_filter_1 with limit=20, Output: ")
	simple_filter_1(*my_values,limit=20)

	print("\n4. Custom Filter Function with limit 5, Output: ")
	fn_5 = list_filter(5)
	fn_5(*my_values)

	print("\n5. Customer Filter Function with limit 20, Output: ")
	fn_20 = list_filter(20)
	fn_20(*my_values)
