from stats import get_word_count
from stats import get_character_count
from stats import sort_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_loc = "books/frankenstein.txt"
    book = get_book_text(book_loc)
    word_count = get_word_count(book)
    character_count = get_character_count(book)
   # sorted_character_count = sort_character_count(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_loc}...")
    print('----------- Word Count ----------')
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(character_count)

main()
