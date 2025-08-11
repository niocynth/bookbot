def gen_report(book_loc, word_count, character_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_loc}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in character_list:
    #    print(f"{character} -----------")
        char_name = character["char"]
        char_count = character["num"]
        print(f"{char_name}: {char_count}")
    
