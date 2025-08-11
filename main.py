import sys
from stats import get_word_count
from stats import get_character_dict
from stats import convert_character_count
from stats import sort_on
from stats import sort_char_list
from report import gen_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # catch invalid args
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_loc = sys.argv.pop()
    book = get_book_text(book_loc)
    word_count = get_word_count(book)
    character_dict = get_character_dict(book)
    char_list = convert_character_count(character_dict)
    character_list = sort_char_list(char_list)
    gen_report(book_loc, word_count, character_list)

main()
