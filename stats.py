def get_book_text (path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def get_word_count(book_content):
    words = len(book_content.split())  
    return words

def get_char_count(book_content):

    lower = book_content.lower()

    count = 0

    char_dict = {}

    for i in lower:
        
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1

            

    return char_dict

def get_sorted(char_dict):
    return char_dict["count"]


def sorted_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=get_sorted)

    return char_list
