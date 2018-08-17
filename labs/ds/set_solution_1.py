def get_consonants(word):
	"""
	Returns a set of consonants in the word
	"""
	return {c for c in word if not c.isspace() and c.lower() not in 'aeiou'}
