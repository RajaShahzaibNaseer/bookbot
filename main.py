from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        get_word_count(file_contents)
        get_character_count(file_contents)

def main():
    path_to_file = "/home/shahzaib/linux-work/bookbot/books/frankenstein.txt"
    get_book_text(path_to_file)

if __name__ == "__main__":
    main()
