def vowel_check(val):
	"""
	This function takes a single character string as input and returns True if it is a vowel, 
	False otherwise.
	"""
	if len(val)>1:
		print ("Error: Input value should be of 1 char. len({v}) = {l}".format(v=val,l=len(val)))
		return
	return val.lower() in "aeiou"
