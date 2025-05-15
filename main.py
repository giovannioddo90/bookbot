from stats import count_words, char_count

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = count_words(text)
    chars_dict = char_count(text)

    print(f"{word_count} words found in the document")
    print(chars_dict)
    
main()