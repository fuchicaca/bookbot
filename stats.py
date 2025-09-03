#takes text as a string, splits into list of words, then returns number of words in text

def word_count(text):
        split_words = len(text.split())
        return split_words

# takes the text as a string, returns the nuber of times each character appears in string

def character_count(text):

#set dictionary to hold characters as keys and counts as values
	counts = {}	
#make text lowercase to avoid reapeats with uppercase letters
	lower_text = text.lower()
#iterate over lowercase string file to seperate by characters then add values
	for ch in lower_text:
		counts[ch] = counts.get(ch,0) + 1
	return counts 

def sort_char_counts(dictionary):
	result = []
	for ch,n in dictionary.items():
		if ch.isalpha():
			item = {"char":ch,"num":n}
			result.append(item)
	

	def sorter(items):
		return items["num"]

	result.sort(reverse=True, key=sorter)
	
	return result 
