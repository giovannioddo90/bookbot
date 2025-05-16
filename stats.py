def count_words(book_text):
    return len(book_text.split())

def char_count(book_text):
    text = book_text.lower()
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

def sort_dict(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    
    sorted_list.sort(key=lambda d: d["num"], reverse=True)

    return sorted_list
