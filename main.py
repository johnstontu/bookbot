def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    chars = get_characters(text)
    char_dict = make_char_dict(chars)
    print(char_dict)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    return text.split()

def get_characters(text):
    return list(text.lower())

def make_char_dict(chars):
    char_dict = {}
    for char in chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


main()