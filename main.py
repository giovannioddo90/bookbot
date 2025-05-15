def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()

    return file_contents

def count_words(book_text):
    words = book_text.split()
    count = 0

    for word in words:
        count += 1
    
    return count

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = count_words(text)
    
    print(f"{word_count} words found in the document")

main()