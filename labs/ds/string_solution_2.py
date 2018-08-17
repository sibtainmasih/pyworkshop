def my_count(sentence):
	"""
	This function takes a sentence input and prints count of letters
	and digits in that sentence
	"""
	l=d=0
	for ch in sentence:
		if ch.isdigit():
			d+=1
		elif ch.isalpha():
			l+=1
	print ("Letters = {l}, Digits = {d}".format(l=l,d=d))	
