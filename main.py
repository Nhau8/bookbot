import sys

from stats import get_word_count
from stats import get_book_text
from stats import get_char_count
from stats import sorted_list




def main(book_path):


    book_content = get_book_text(book_path)     

    word_count = get_word_count(book_content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    char_list = sorted_list(get_char_count(book_content))
    for item in char_list:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")






if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]
    main(book_path)