def my_char_index_fn_1(text, character):
	"""
	This function returns a list of index postions of the `character` in `text`
	"""
	return [i for i in range(len(text)) if text[i] == character]


# Following is more pythonic

def my_char_index_fn_2(text, character):
	"""
	This function returns a list of index positions of the `character` in `text`
	"""
	return [i for i,c in enumerate(text) if c == character]
