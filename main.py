import sys
from stats import count_words, char_count, sort_dict

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    text = get_book_text(book)
    word_count = count_words(text)
    chars_dict = char_count(text)
    sort_list = sort_dict(chars_dict) 

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sort_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
