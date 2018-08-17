def is_panagram(sentence):
	"""
	This function takes a sentence as input and returns `True` if it is panagram, `False` otherwise.
	"""
	sentence = set(sentence.lower())
	alpha = [ch for ch in sentence if ord(ch) in range(ord('a'),ord('z')+1)]
	return len(alpha)==26  
