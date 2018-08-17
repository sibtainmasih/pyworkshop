def histogram(values):
	"""
	This functions takes a list `values` as input and prints histogram accordingly
	"""
	for val in values:
		print("*"*val)

def histogram_1(*values):
	"""
	This is same has histogram function. But here -
	Input in a tuple `values`. While calling this function user can specify any number of int arguments.
	"""
	for val in values:
		print("*"*val)
