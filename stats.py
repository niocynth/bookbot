def get_word_count(string):
    word_count = 0
    words = string.split()
    for word in words:
        word_count += 1
    return word_count

def get_character_dict(string):
    character_dict = {}
    string = string.lower()
    characters = list(string)
    for character in characters:
        if character == " " or character == "\n":
            pass
        elif character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict

def convert_character_count(character_count):
    char_list = []
    for character in character_count:
        ind_count = {}
        count = character_count[character]
        char_list.append({"char": character, "num": count})
    return char_list

def sort_on(items):
    return items["num"]

def sort_char_list(char_list):
    char_list.sort(reverse=True, key=sort_on) 
    return char_list