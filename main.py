from stats import get_num_words
from stats import count_characters
from stats import sort_on
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print(f"{num_words} words found in the document")
    chars = count_characters(text)
    chars_list = list(chars.items())
    chars_list.sort(reverse=True, key=sort_on)
    for key, value in chars_list:
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
