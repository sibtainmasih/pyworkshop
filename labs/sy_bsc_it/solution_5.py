def common_check(input_list_1, input_list_2):
	"""
	Returns `True` if both the lists have at least 1 common element
	"""
	return len(set(input_list_1) & set(input_list_2)) > 0

def common_check_2(input_list_1, input_list_2):
	"""
	Returns `True` if both the lists have at least 1 common element
	"""
	return not (set(input_list_1)).isdisjoint(set(input_list_2))
