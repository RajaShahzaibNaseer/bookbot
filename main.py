from stats import *
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        report_maker(file_contents)


def report_maker(file_contents):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_word_count(file_contents)
    print("--------- Character Count -------")
    sorted_list = get_character_count(file_contents)
    for dictionary in sorted_list:
        if str.isalpha(dictionary["char"]):
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")


def main():
    # path_to_file = "/home/shahzaib/linux-work/bookbot/books/frankenstein.txt"
    if sys.argv[0]:
        get_book_text(sys.argv[0])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit()


if __name__ == "__main__":
    main()
