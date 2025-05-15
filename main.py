from stats import count_words

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = count_words(text)
    
    print(f"{word_count} words found in the document")

main()