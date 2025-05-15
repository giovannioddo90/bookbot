def count_words(book_text):
    words = book_text.split()
    count = 0

    for word in words:
        count += 1
    
    return count