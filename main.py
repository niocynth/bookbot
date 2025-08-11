from stats import get_word_count
from stats import get_character_count
from report import gen_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_loc = "books/frankenstein.txt"
    book = get_book_text(book_loc)
    word_count = get_word_count(book)
    character_list = get_character_count(book)
    gen_report(book_loc, word_count, character_list)

main()
