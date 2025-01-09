def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    chars = get_characters(text)
    char_dict = make_char_dict(chars)
    sorted_char_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    word_count = get_word_count(text)
    print("--- begin report of books/frenkenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for key, count in sorted_char_dict:
        print(f"The {key} character was found {count} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_characters(text):
    abc = "qwertyuiopasdfghjklzxcvbnm"
    letters =  list(text.lower())
    filtered_letters = [item for item in letters if item in abc]
    return filtered_letters

def make_char_dict(chars):
    char_dict = {}
    for char in chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
    

main()