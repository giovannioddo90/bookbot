def count_words(book_text):
    words = book_text.split()
    count = 0

    for word in words:
        count += 1
    
    return count

def char_count(book_text):
    words = book_text.lower()

    char_count = {}

    for character in words:
        if character not in char_count:
            char_count[character] = 1
        else:
            char_count[character] += 1

    return char_count

