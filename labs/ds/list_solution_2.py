def my_flat_list_fn(input_list):
	"""
	This function takes a nested list and returns a new flatten list
	"""
	return [el for sub_list in input_list for el in sub_list]
