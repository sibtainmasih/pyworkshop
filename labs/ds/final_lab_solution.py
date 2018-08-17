# 1. Read story.txt file in a variable and print its text.
FILE_PATH = "story.txt"
with open(FILE_PATH, 'r') as input_stream:
	content = input_stream.read()

# 2. Replace punctuation characters by single space(' ') and print text.
from string import punctuation
for char in punctuation:
	content = content.replace(char, ' ')

# 3. Replace two spaces('  ') by single space(' ') and print text.
content = content.replace(' '*2, ' ')

# 4. From text, create an array of words and print it.
words = content.split(' ')
# print (words)


# 5. Create a dictionary representing frequency distribution of each word.
# 6. Don't add commonly occuring words to the frequency distribution dictionary. Use following as exclusion list.
# 7. Only add words with minimum 4 characters to frequency distribution dictionary.
f_dist = {}

EXCLUSION_LIST = ['a', 'an', 'the', 'then', 'that', 'he', 'she', 'it', '\n']

for word in words:
	if word not in EXCLUSION_LIST and len(word)>3:
		f_dist[word] = f_dist.get(word,0) + 1

# 8. Print the dictionary in the lexical order of keys.
ordered_keys = sorted(f_dist.keys())

# for key in ordered_keys:
#	print ("{key} => {value}".format(key=key, value=f_dist[key]))

# 9. Print words in descending order of their frequency.
words_by_frequency = sorted(f_dist.items(), key=lambda val: val[1], reverse=True)
# print (words_by_frequency)

# 10. Show me top 5 occuring words. Are they representative of the story text?
print (words_by_frequency[:5])
