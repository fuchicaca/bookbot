from stats import word_count
from stats import character_count
from stats import sort_char_counts

#takes filepath as input and returns the contents of the file as a string


def get_book_text(filepath):

	with open(filepath) as f:
		file_contents = f.read()	

	return file_contents
	

def main():

	text = get_book_text("books/frankenstein.txt")
	num_words = word_count(text)
	ch_count = character_count(text)
	descending = sort_char_counts(ch_count)
	
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in descending:
		print(f"{item["char"]}: {item["num"]}")
	print("============= END ===============")
if __name__ == "__main__":
	main()
