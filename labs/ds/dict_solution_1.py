capitals = {'India': 'Delhi', 'Bangladesh': 'Dhaka', 'England': 'London', 'Canada': 'Ottawa'}

def print_dict(keys):
	"""
	Prints content of dictionary in the order of input `keys` list
	"""
	for key in keys:
		print ("{country} => {capital}".format(country=key,capital=capitals[key]))

print("a. Lexical Order by Country Name.")
keys = sorted(capitals.keys())
print_dict(keys)


print("b. Descending Order of Country Name length")
keys = sorted(capitals.keys(), key=lambda val: len(val), reverse=True)
print_dict(keys)
