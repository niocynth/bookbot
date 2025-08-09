def get_word_count(string):
    word_count = 0
    words = string.split()
    for word in words:
        word_count += 1
    return f"{word_count} words found in the document"

def get_character_count(string):
    character_count = {}
    string = string.lower()
    characters = list(string)
    for character in characters:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count

def sort_on(character_count):
    return character_count[1]

def sort_character_count(character_count):
    character_count.sort(reverse=True, key=character_count[1])
    return character_count