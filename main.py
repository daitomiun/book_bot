import sys

def main():
    file_path = "./books/frankenstein.txt"
    file_contents = open_file(file_path)

    num_words = get_num_words(file_contents)
    print(f"--- Begin report of {file_path}---")
    print(f"{num_words} words found in this document")

    repeated_chars = get_repeated_chars(file_contents.lower())

    print("---- List of repeated characters ----")
    generate_report(repeated_chars)
    print("--- End report ---")


def get_num_words(words):
    return len(words.split())

def get_repeated_chars(text):
    repeated_chars = {}
    for char in text:
        if char.isalpha():
            if (char in repeated_chars):
                repeated_chars[char] += 1
            else: 
                repeated_chars[char] = 1

    return repeated_chars


def generate_report(chars_dict):

    sorted_chars_dict = dict(sorted(chars_dict.items(), key=lambda x:x[1], reverse=True))

    print(sorted_chars_dict)
    for char in sorted_chars_dict:
        print(f"The {char} character was found {sorted_chars_dict[char]} times")

def open_file(path):
    with open(path) as f:
            return f.read()


if __name__ == '__main__':
    sys.exit(main())
